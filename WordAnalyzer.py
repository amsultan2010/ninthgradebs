H=len
G=range
D=ord
def A(g,w,a):
	M='A';I=w;E=a;B=g;F=[-2]*5;J=[False]*5
	for A in G(H(B)):
		if B[A]==I[A]:F[A]=1;J[A]=True;C=D(B[A])-D(M);E[C]=1
	for A in G(H(B)):
		if F[A]!=1:
			K=-1
			for L in G(H(I)):
				if not J[L]and B[A]==I[L]:K=L
			if K!=-1:
				F[A]=0;J[K]=True;C=D(B[A])-D(M)
				if E[C]!=1:E[C]=0
	for A in G(H(B)):
		if F[A]==-2:
			F[A]=-1;C=D(B[A])-D(M)
			if E[C]==-2:E[C]=-1
	return F,E