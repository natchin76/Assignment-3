#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#include<gsl/gsl_fft_complex.h>
int main(){
	int n=256;
	double xmin=-50,xmax=50;
	double dx=(xmax-xmin)/(n-1);
	double k[n],x[n];
	double f_q[2*n],f_t_q_r[n],f_t_q_i[n];
	for (int i = 0; i < n; ++i)
	{
		x[i]=xmin+i*dx;
	}
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
		if (x[i]==0.0)
		{
			f_q[2*i]=0.0;
		}
		else
		{
			f_q[2*i]=sin(x[i])/x[i];
	    }
		
	}
	gsl_complex_packed_array data = f_q;
	gsl_fft_complex_radix2_forward (f_q, 1, 256);
	for (int i = 0; i < n; ++i)
	{
		f_t_q_r[i]=dx*sqrt(1/(2*M_PI))*(cos(k[i]*xmin)*f_q[2*i]+sin(k[i]*xmin)*f_q[2*i+1]);
		f_t_q_i[i]=dx*sqrt(1/(2*M_PI))*(cos(k[i]*xmin)*f_q[2*i+1]-sin(k[i]*xmin)*f_q[2*i]);
	}





	for (int i = 0; i < n; ++i)
	{
		printf("%f\n",f_t_q_r[i]);
	}
	
return(0);


}