l = 10;
m = 9.99999999;

rho = l/m;
K = 10;

po = (1- rho)/(1-rho^(K+1));
nbar = po * 0;
p1to10 = zeros(1,10);


for i = 1:10
	p1to10(i) = po * (rho)^i; 
	nbar += p1to10(i) * i;
endfor

p1to10
nbar