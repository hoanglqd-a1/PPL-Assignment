%main program


reduce_prog([Var,Func,B]) :-
		create_env(Var,env([[]],false),Env1),
		create_env(Func,Env1,Env2),
		reduce_stmt(config(B,Env2),_).
											
%check if X has been declared in the first list of the environment
has_declared(X,[id(X,_,_,_)|_],_) :- !.
has_declared(X,[_|L],R) :- has_declared(X,L,R).

%create a symbol table from the list of variable or constant declarations
create_env([],L,L).

create_env([var(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|_],env([L1|_],_),_):-has_declared(X,L1,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,var,Y,nil)|L1]|L2],T),L3).

create_env([const(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|_],env([L1|_],_),_):-has_declared(X,L1,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|L],env([L1|L2],T),L3):- type_of(Y,Type),create_env(L,env([[id(X,const,Type,Y)|L1]|L2],T),L3).

create_env([func(I,P,R,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_function(func(I,P,R,B))).
create_env([func(I,P,R,B)|_],env([L1|_],_),_):-has_declared(I,L1,_),!,throw(redeclare_function(func(I,P,R,B))).
%create_env([func(I,P,R,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,func,[P,R],B)|L1]|L2],T),L3),check_param(P,[]).
create_env([func(I,P,R,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,func,[P,R],B)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([proc(I,P,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|_],env([L1|_],_),_):-has_declared(I,L1,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,proc,[P|nil],B)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([par(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(par(X,Y))).
create_env([par(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,par,Y,nil)|L1]|L2],T),L3).

reduce_stmt(config([call(writeInt,[X])],_),_) :-
		reduce_all(config(X,Env),config(V,Env)),
		integer(V),!,
		write(V)
		.

reduce_stmt(config([call(writeReal,[X])],_),_) :-
		reduce_all(config(X,Env),config(V,Env)),
		float(V),!,
		write(V)
		.

reduce_stmt(config([call(writeStr,[X])],_),_) :-
		reduce_all(config(X,Env),config(V,Env)),
		string(V),!,
		write(V)
		.

reduce_stmt(config([call(writeBool,[X])],_),_) :-
		reduce_all(config(X,Env),config(V,Env)),
		boolean(V),!,
		write(V)
		.
	
reduce_all(config(V,Env),config(V,Env)):- integer(V),!.
reduce_all(config(V,Env),config(V,Env)):- float(V),!.
reduce_all(config(V,Env),config(V,Env)):- string(V),!.
reduce_all(config(V,Env),config(V,Env)):- boolean(V),!.
reduce_all(config(E,Env),config(E2,Env)):-
		reduce(config(E,Env),config(E1,Env)),!,
		reduce_all(config(E1,Env),config(E2,Env)).

reduce(config(sub(E),Env),config(R,Env)) :- 
			reduce_all(config(E,Env),config(V,Env)),
			R is -V.
reduce(config(add(E1,E2),Env),config(R,Env)) :-
			reduce_all(config(E1,Env),config(V1,Env)),
			reduce_all(config(E2,Env),config(V2,Env)),
			R is V1+V2.
reduce(config(sub(E1,E2),Env),config(R,Env)) :-
			reduce_all(config(E1,Env),config(V1,Env)),
			reduce_all(config(E2,Env),config(V2,Env)),
			R is V1-V2.
reduce(config(times(E1,E2),Env),config(R,Env)) :-
			reduce_all(config(E1,Env),config(V1,Env)),
			reduce_all(config(E2,Env),config(V2,Env)),
			R is V1*V2.
reduce(config(rdiv(E1,E2),Env),config(R,Env)) :-
			reduce_all(config(E1,Env),config(V1,Env)),
			reduce_all(config(E2,Env),config(V2,Env)),
			R is V1/V2.

boolean(true).
boolean(false).
type_of(X,integer):- integer(X),!.
type_of(X,real):- float(X),!.
type_of(X,string):- string(X),!.
type_of(X,bool):- boolean(X),!.