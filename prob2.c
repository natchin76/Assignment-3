#include <stdio.h>
#include<stdlib.h>
#include<fftw3.h>
#include<math.h>
int main(){
	int n=256;
	double xmin=-50,xmax=50;
	double dx=(xmax-xmin)/(n-1);
	double k[n],x[n];
	fftw_complex w_p[n], tw_q[n],tw_q_n[n],f_t_q[n];
	fftw_plan p; 
	for (int i = 0; i < n; ++i)
	{
		x[i]=xmin+i*dx;
	}
	for (int i = 0; i < n; ++i)
	{
		if (x[i]==0.0)
		{
			w_p[i][0]=0.0;
		}
		else
		{
			w_p[i][0]=sin(x[i])/x[i];
	    }
		w_p[i][1]=0;
	}

	p=fftw_plan_dft_1d(n,w_p,tw_q,FFTW_FORWARD,FFTW_ESTIMATE);
	fftw_execute(p);

	for (int i = 0; i < n; ++i)
	{
		tw_q_n[i][0]=tw_q[i][0]/sqrt(n);
		tw_q_n[i][1]=tw_q[i][1]/sqrt(n);
	}
	fftw_destroy_plan(p);
	for (int i = 0; i < n; ++i)
	{	if (i<n/2)
	{
		k[i]= 2*M_PI*(i*1.0/(n*dx));
	}	else{
		k[i]= 2*M_PI*((i-n)/(n*dx));
		}	 
		
	}
	for (int i = 0; i < n; ++i)
	{
		f_t_q[i][0]=dx*sqrt(n/(2*M_PI))*(cos(k[i]*xmin)*tw_q_n[i][0]+sin(k[i]*xmin)*tw_q_n[i][1]);
		f_t_q[i][1]=dx*sqrt(n/(2*M_PI))*(cos(k[i]*xmin)*tw_q_n[i][1]-sin(k[i]*xmin)*tw_q_n[i][0]);
	}

	for (int i = 0; i < n; ++i)
	{
		printf("%lf %lf %lf\n",f_t_q[i][0],k[i],tw_q[i][0]);
	}


	return(0);


}