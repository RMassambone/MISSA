#ifndef STOCHASTIC_ERRORS_INLINE_H
#define STOCHASTIC_ERRORS_INLINE_H

/**
   \file stochastic_errors_inline.h Implements the stochastic errors.
*/

#include "stochastic_errors.h"
#include <algorithm>
#include <vector>
#include <random>

///Constructor
/**
\param type This flag is related to the test we desire to run.
\param shuffled_agents The shuffled set of agents' indexes.
*/

stochastic_errors::stochastic_errors( int type, std::vector< int > shuffled_agents )
: type_( type ), shuffled_agents_( shuffled_agents )
{}

/// Obtain the random noise vector.
/**
\param k Iteration;
\param index Index i related to the component function f_i.
\param eps Random noise vector.
*/
void stochastic_errors::get_error( int k, int index, std::vector< double > & eps ){
	
	int seed = 234 * k;
	std::default_random_engine generator(seed);
	double X;
	double Y;
	std::uniform_real_distribution< double > unif_dist(0.0,1.0);
	std::normal_distribution< double > normal_dist(0.0,1.0);
	
	if ( type_ == 1 ){
		for (int i = 0; i < eps.size(); i++){
			eps[i] = 0.0;
		}
	}
	if ( type_ == 2 ){
		for (int i = 0; i < eps.size(); i++){
			X = unif_dist(generator);
			eps[i] = X / (k + 1);
		}
	}
	if ( type_ == 3 ){
		for (int i = 0; i < eps.size(); i++){
			X = unif_dist(generator);
			eps[i] = 0.1 * X;
		}
	}
	if ( type_ == 4 ){
		for (int i = 0; i < eps.size(); i++){
			X = unif_dist(generator);
			eps[i] = 0.01 * X;
		}
	}
	if ( type_ == 5 ){
		for (int i = 0; i < eps.size(); i++){
			Y = normal_dist(generator);
			eps[i] = 0.1 * Y;
		}
	}
	if ( type_ == 6 ){
		for (int i = 0; i < eps.size(); i++){
			Y = normal_dist(generator);
			eps[i] = 0.01 * Y;
		}
	}
	if ( type_ == 7 ){
		if ( index == shuffled_agents_[0] || index == shuffled_agents_[1] || index == shuffled_agents_[2] || index == shuffled_agents_[3] ){
			for (int i = 0; i < eps.size(); i++){
				X = unif_dist(generator);
				eps[i] = 0.1 * X;
			}
		}
		else{
			for (int i = 0; i < eps.size(); i++){
				Y = normal_dist(generator);
				eps[i] = 0.1 * Y;
			}
		}
	}
	if ( type_ == 8 ){
		if ( index == shuffled_agents_[0] || index == shuffled_agents_[1] || index == shuffled_agents_[2] || index == shuffled_agents_[3] ){
			for (int i = 0; i < eps.size(); i++){
				Y = normal_dist(generator);
				eps[i] = 0.01 * Y;
			}
		}
		else{
			for (int i = 0; i < eps.size(); i++){
				X = unif_dist(generator);
				eps[i] = 0.01 * X;
			}
		}
	}
}

#endif
