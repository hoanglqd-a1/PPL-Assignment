%main program


reduce_prog([Var,Func,Stmt]) :-
		create_env(Var,env([[]],false),Env1),
		create_env(Func,Env1,Env2),
		Env2 = env(T,_),
		reduce_stmt(config(Stmt,env([[]|T],_)),_).
											
%check if X has been declared in the first list of the environment
has_declared(X,[id(X,_,_,_)|_],_) :- !.
has_declared(X,[_|L],R) :- has_declared(X,L,R).

%create a symbol table from the list of variable or constant declarations
create_env([],L,L).

create_env([var(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,var,Y,nil)|L1]|L2],T),L3).

create_env([const(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|L],env([L1|L2],T),L3):- reduce_all(config(Y,env([L1|L2],T)),config(V,env([L1|L2],T))),type(V,Type),create_env(L,env([[id(X,const,Type,V)|L1]|L2],T),L3).

create_env([func(I,P,R,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_function(func(I,P,R,B))).
create_env([func(I,P,R,B)|_],env([L1|_],_),_):- has_declared(I,L1,_),!,throw(redeclare_function(func(I,P,R,B))).
create_env([func(I,P,R,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,func,[P,R],B)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([proc(I,P,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|_],env([L1|_],_),_):- has_declared(I,L1,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,proc,P,B)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([par(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(par(X,Y))).
create_env([par(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,par,Y,nil)|L1]|L2],T),L3).
create_env([],E,[],E):- !.
create_env([par(X,Y)|L],env([L1|L2],T),[V|VTail],L3):- create_env(L,env([[id(X,par,Y,V)|L1]|L2],T),VTail,L3).

reduce_stmt(config([],Env),Env) :- !.

reduce_stmt(config([var(Name,Type)|_],Env),_) :- 
		Env = env([L1|_],_),has_declared(Name,L1,_),
		!,throw(redeclare_identifier(var(Name,Type))).
reduce_stmt(config([var(Name,Type)|Tail],Env),L) :-
		Env = env([L1|L2],T),
		reduce_stmt(config(Tail,env([[id(Name,var,Type,nil)|L1]|L2],T)),L).

reduce_stmt(config([const(Name,Expr)|_],Env),_) :- 
		Env = env([L1|_],_),has_declared(Name,L1,_),
		!,throw(redeclare_identifier(const(Name,Expr))).
reduce_stmt(config([const(Name,Expr)|Tail],Env),L) :-
		Env = env([L1|L2],T),
		reduce_all(config(Expr,Env),config(Value,Env)),
		type(Value,Type),
		reduce_stmt(config(Tail,env([[id(Name,const,Type,Value)|L1]|L2],T)),L).

reduce_stmt(config([call(Name,[Expr])|Tail],Env),T) :- is_builtin(Name,_),!,
		reduce_all(config(Expr,Env),config(Value,Env)),
		p_call_builtin(Name,[Value]),
		reduce_stmt(config(Tail,Env),T).
reduce_stmt(config([call(Name,Exprs)|Tail],Env),T) :- 
		Env = env(E,T),
		last(E,E1),
		(getprocedure(Name,E1,Proc) -> true; throw(undeclare_procedure(call(Name,Exprs)))),
		Proc = id(Name,proc,Params,Body),
		(length(Params,L),length(Exprs,L) -> true; throw(wrong_number_of_argument(call(Name,Exprs)))),
		calculateArgs(Exprs,Env,Values),
		create_env(Params,env([[]|E],_),Values,Env1),
		reduce_stmt(config(Body,Env1),_),
		reduce_stmt(config(Tail,Env),T).

reduce_stmt(config([assign(Name,Expr)|STail],Env1),_) :-
		find_and_assign(assign(Name,Expr),Env1,Env2,Env1),
		reduce_stmt(config(STail,Env2),_).

find_and_assign(assign(Name,Expr),Env1,Env2,Env) :-
		Env1 = env([[id(Name,Kind,Type,_    )|Tail]|LTail],_),
		Env2 = env([[id(Name,Kind,Type,Value)|Tail]|LTail],_),
		!,
		reduce_all(config(Expr,Env),config(Value,Env)),(
			Kind \= const; throw(cannot_assign(assign(Name,Value)))
		),(
			type(Value,Type), !;
			throw(type_mismatch(assign(Name,Value)))
		).
find_and_assign(assign(Name,Expr),Env1,Env2,Env) :-
		Env1 = env([[Id|Tail1]|LTail1],_),
		Env2 = env([[Id|Tail2]|LTail2],_),
		!,find_and_assign(assign(Name,Expr),env([Tail1|LTail1],_),env([Tail2|LTail2],_),Env).
find_and_assign(assign(Name,Expr),Env1,Env2,Env) :-
		Env1 = env([[]|LTail1],_),
		Env2 = env([[]|LTail2],_),
		!,find_and_assign(assign(Name,Expr),env(LTail1,_),env(LTail2,_),Env).
find_and_assign(assign(Name,Expr), env([],_), _, _) :-
		!,throw(undeclare_identifier(assign(Name,Expr))).

getprocedure(Name, [id(Name, proc, P, B)|_], id(Name, proc, P, B)) :- !.
getprocedure(Name, [_|T], Proc) :-
		getprocedure(Name, T, Proc).
		
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
reduce(config(I,Env),config(R,Env)):-
		getvalue(I,Env,R).

getvalue(I, Env, R) :-
		Env = env([[id(I, _, _, R)|_]|_], _),
		!,
		(R \= nil -> true; throw(undeclare_identifier(I))).
getvalue(I, env([[_|T]|TT], _), R) :-
		!,
		getvalue(I, env([T|TT], _), R).
getvalue(I, env([[]|TT], _), R) :-
		!,
		getvalue(I, env(TT, _), R).
getvalue(I, env([[]], _), _) :-
    	throw(undeclare_identifier(I)).

calculateArgs([], _, []) :- !.
calculateArgs([Expr|ETail], Env, [Value|VTail]) :-
    reduce_all(config(Expr, Env), config(Value, Env)),
    calculateArgs(ETail, Env, VTail).

reduce_all(config(V,Env),config(V,Env)):- (integer(V);float(V);string(V);boolean(V)),!.
reduce_all(config(E,Env),config(E2,Env)):-
		reduce(config(E,Env),config(E1,Env)),!,
		reduce_all(config(E1,Env),config(E2,Env)).

boolean(true).
boolean(false).
type(X,integer):- integer(X),!.
type(X,real):- float(X),!.
type(X,string):- string(X),!.
type(X,bool):- boolean(X),!.
