clear

// Loi normale
function [x]=normale(y,m,s2)
  x=%e^(-(y-m).^2/2/s2)/sqrt(2*%pi*s2)
endfunction;

// Ouvrir le fichier de données (nombre de crabes par intervalle)
x=fscanfMat('crabe.txt');
x=x;

// intervalles
y=.580+.002+.004*[0:28];
yM=y+.002;
ym=y-.002;
Max=25;

// Dessiner la loi normale correspondante
// A FAIRE

// Tracer l'histogramme
// A FAIRE

// Données
pi0=[1; 3]/2/2;
pi=pi0;
mu=[.57; .67];
s2=[1 ;1]/10000;

rho=ones(2,1000);

// Algorithme EM pour les crabes 
//------------------------------

N=1000;
R=zeros(5,N+1);
R(:,1)=[mu(1);mu(2);pi(1);s2(1);s2(2)];

for k=1:N;
  // Iteration k
  // A FAIRE
end;

// Affichages
// A FAIRE
