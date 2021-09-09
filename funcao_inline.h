#ifndef FUNCAO_INTERFACE_INLINE_H
#define FUNCAO_INTERFACE_INLINE_H

#include "funcao.h"
#include <math.h>

///Construtor
/**
\param A Matriz do sistema
\param b termos independentes
*/
residual_norm_one::residual_norm_one( const std::vector< std::vector< double > >& A, const std::vector< double > & b, const std::vector< double > & omega )
   :  A_( A ), b_( b ), omega_( omega )
{}

/// Avalia a funcao.
/**
\return Valor da funcao.
\param x Vetor a ter funcao calculada.
*/
double residual_norm_one::eval( const std::vector< double >& x ) const
{
   double sum = 0.0;
   for (unsigned int i = 0; i < A_.size(); i++){
	   double aux = 0.0;
       for (unsigned int j = 0; j < A_[i].size(); j++){
           aux += A_[i][j] * x[j];
       }
       aux = aux - b_[i];
       sum += omega_[i] * fabs(aux);
   }
   return( sum );
}

/// Calcula subgradiente de f_i em x.
/**
\param x Vetor a ser calculado o subgradiente de f_i.
\param subgrad Subgradiente.
\param i Indice da parcela f_i.
*/
void residual_norm_one::subgrad_parcel( const std::vector< double >& x, std::vector< double >& subgrad, int index) const
{
    	
	double aux = 0.0;
    for (unsigned int j = 0; j < A_[index].size(); j++){
        aux += A_[index][j] * x[j];
    }
    aux = aux - b_[index];
	
    if(aux > 0.0){
        subgrad = A_[index];
    }
    
    if(aux < 0.0){
		for (unsigned int j = 0; j < subgrad.size(); j++)
            subgrad[j] = -A_[index][j];
    }
    
    if(aux == 0.0){
        for (unsigned int j = 0; j < subgrad.size(); j++)
            subgrad[j] = 0.0;
    }
}

/// Calcula subgradiente de \omega_i * f_i em x.
/**
\param x Vetor a ser calculado o subgradiente de \omega_i * f_i.
\param subgrad Subgradiente.
\param i Indice da parcela f_i.
*/
void residual_norm_one::subgrad_parcel_weighted( const std::vector< double >& x, std::vector< double >& subgrad, int index) const
{
    double aux = 0.0;
    for (unsigned int j = 0; j < A_[index].size(); j++){
        aux += omega_[index] * A_[index][j] * x[j];
    }
    aux = aux - omega_[index] * b_[index];
    if(aux > 0.0){
        for (unsigned int j = 0; j < subgrad.size(); j++)
            subgrad[j] = omega_[index] * A_[index][j];
    }
    if(aux < 0.0){
        for (unsigned int j = 0; j < subgrad.size(); j++)
            subgrad[j] = - omega_[index] * A_[index][j];
    }
    if(aux == 0.0){
        for (unsigned int j = 0; j < subgrad.size(); j++)
            subgrad[j] = 0.0;
    }
   
}

#endif
