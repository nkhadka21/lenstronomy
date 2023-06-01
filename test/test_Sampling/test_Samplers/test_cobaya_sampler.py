__author__ = 'nataliehogg'

import pytest
import numpy as np

from lenstronomy.Sampling.Samplers.cobaya_sampler import CobayaSampler

_outpath = 'cobaya_chain'

@pytest.fixture
def import_fixture(simple_einstein_ring_likelihood):
    """

    :param simple_einstein_ring_likelihood_2d: fixture
    :return:
    """
    likelihood, kwargs_truths = simple_einstein_ring_likelihood
    means = likelihood.param.kwargs2args(**kwargs_truths)
    sigmas = np.ones_like(means)*0.1
    sampler = CobayaSampler(likelihood_module=likelihood, mean_start=means, sigma_start=sigmas)
    return sampler, likelihood, means, sigmas

class TestCobayaSampler(object):
    """
    test cobaya
    """

    def setup_method(self): # what is this for?
        pass

    def test_sampler(self, import_fixture):

        sampler, likelihood, means, sigmas = import_fixture

        updated_info, sampler_name, best_fit_values = sampler.run()

if __name__ == '__main__':
    pytest.main()
