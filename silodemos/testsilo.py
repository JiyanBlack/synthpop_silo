import pandas as pd

import numpy as np

from csynthpop import zone_synthesizer as zs

hh_marginal_file = './data/hh_marginals.csv'
person_marginal_file = './data/person_marginals.csv'
hh_sample_file = './data/household_sample.csv'
person_sample_file = './data/person_sample.csv'

def convert_to_str(margin, sample):
    colist = []
    for acol in margin.columns:
        colist.append(acol[0])
    colist = np.unique(colist)
    for acol in colist:
        if acol in sample.columns:
            sample[acol] = sample[acol].astype(str)
    return sample

hh_marg, p_marg, hh_sample, p_sample, xwalk = zs.load_data(hh_marginal_file, person_marginal_file, hh_sample_file, person_sample_file)

hh_sample = convert_to_str(hh_marg,hh_sample)
p_sample = convert_to_str(p_marg,p_sample)

all_households, all_persons, all_stats = zs.synthesize_all_zones(hh_marg, p_marg, hh_sample, p_sample, xwalk)

all_households.to_csv('./data/output/all_households.csv')
all_persons.to_csv('./data/output/all_persons.csv')

all_stats.to_csv('./data/output/all_stats.csv')