#ifndef MARKOV_CHAIN_INLINE_H
#define MARKOV_CHAIN_INLINE_H

/**
   \file markov_chain_inline.h Implements the Markov chain state.
*/

#include "markov_chain.h"
#include <algorithm>
#include <vector>
#include <random>

struct compare
{
	double key;
	compare(double const &i): key(i) {}
	 
	bool operator()(double const &i) {
		return (i > key);
	}
};

///Constructor
/**
 \param P Transition probability matrix.
 \param init_dist Initial distribution.
 */
markov_chain::markov_chain( std::vector< std::vector< double > > P, std::vector< double > init_dist )
:  P_( P ), init_dist_( init_dist )
{}

/// Compute the next state of a Markov chain.
/**
 * \param k Time;
 * \param cur_state State with respect to the time k-1.
 */

int markov_chain::eval_MC_time( int k, int cur_state ){
	
	int seed = 123 * k;
	std::default_random_engine generator(seed);
	std::uniform_real_distribution< double > distribution(0.0,1.0);
	double r;
	
	std::vector< double > cumsum( init_dist_.size() );
	
	int next_state;
	
	if( k == 0 ){
		r = distribution(generator);
		cumsum[0] = init_dist_[0];
		
		for (int i = 1; i < init_dist_.size(); i++){
			cumsum[i] = cumsum[i-1] + init_dist_[i];
		}
		
		auto itr = std::find_if(cumsum.cbegin(), cumsum.cend(), compare(r));
		next_state = std::distance(cumsum.cbegin(), itr);
	}
	else{
		
		std::vector< double > cur_distribution( init_dist_.size() );
		
		for (int j = 0; j < init_dist_.size(); j++){
			cur_distribution[j] = P_[cur_state][j];
		}
		
		r = distribution(generator);
		
		cumsum[0] = cur_distribution[0];
		
		for (int i = 1; i < init_dist_.size(); i++){
			cumsum[i] = cumsum[i-1] + cur_distribution[i];
		}
		
		auto itr = std::find_if(cumsum.cbegin(), cumsum.cend(), compare(r));
		next_state = std::distance(cumsum.cbegin(), itr);
	}
	
	return( next_state );	
}

#endif
