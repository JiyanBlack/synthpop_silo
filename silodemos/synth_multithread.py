import pandas as pd

import synthpop.zone_synthesizer as zs

hh_marginal_file = './data/hh_marginals.csv'
person_marginal_file = './data/person_marginals.csv'
hh_sample_file = './data/household_sample.csv'
person_sample_file = './data/person_sample.csv'

hh_marg, p_marg, hh_sample, p_sample, xwalk = zs.load_data(hh_marginal_file, person_marginal_file, hh_sample_file, person_sample_file)