#!/usr/bin/python3
import random
import math
import numpy


def get_swiss_roll_dataset(numOfSamples):
    sample_list = []
    for x in range(0, numOfSamples):
        noise_test = random.random()
        if noise_test < 0.1:  # Add gaussian noise
            noise_1 = numpy.random.normal(0, 0.1)
            noise_2 = numpy.random.normal(0, 0.1)
            noise_3 = numpy.random.normal(0, 0.1)
            sample_list.append([noise_1, noise_2, noise_3])
            continue
        p_i = random.random()
        q_i = random.random()
        t_i = math.pi * 3 / 2 * (1 + 2 * p_i)
        x_i = [(t_i * math.cos(t_i)), t_i * math.sin(t_i), 30 * q_i]
        sample_list.append(x_i)
    return sample_list


def get_broken_swiss_roll_dataset(numOfSamples):
    sample_list = []
    for x in range(0, numOfSamples):
        noise_test = random.random()
        if noise_test < 0.1:  # Add gaussian noise
            noise_1 = numpy.random.normal(0, 0.1)
            noise_2 = numpy.random.normal(0, 0.1)
            noise_3 = numpy.random.normal(0, 0.1)
            sample_list.append([noise_1, noise_2, noise_3])
            continue
        while True:
            p_i = random.random()
            q_i = random.random()
            t_i = math.pi * 3 / 2 * (1 + 2 * p_i)
            if p_i >= (4 / 5) or p_i <= (2 / 5):
                break
        x_i = [(t_i * math.cos(t_i)), t_i * math.sin(t_i), 30 * q_i]
        sample_list.append(x_i)
    return sample_list


def get_helix_dataset(numOfSamples):
    sample_list = []
    for x in range(0, numOfSamples):
        noise_test = random.random()
        if noise_test < 0.1:  # Add gaussian noise
            noise_1 = numpy.random.normal(0, 0.1)
            noise_2 = numpy.random.normal(0, 0.1)
            noise_3 = numpy.random.normal(0, 0.1)
            sample_list.append([noise_1, noise_2, noise_3])
            continue
        p_i = random.random()
        x_i = [(2 + math.cos(8 * p_i)) * math.cos(p_i), (2 + math.cos(8 * p_i)) * math.sin(p_i), math.sin(8 * p_i)]
        sample_list.append(x_i)
    return sample_list


def get_twin_peaks(numOfSamples):
    sample_list = []
    for x in range(0, numOfSamples):
        noise_test = random.random()
        if noise_test < 0.1:  # Add gaussian noise
            noise_1 = numpy.random.normal(0, 0.1)
            noise_2 = numpy.random.normal(0, 0.1)
            noise_3 = numpy.random.normal(0, 0.1)
            sample_list.append([noise_1, noise_2, noise_3])
            continue
        p_i = random.random()
        q_i = random.random()
        x_i = [1 - 2 * p_i, math.sin(math.pi - 2 * math.pi * p_i), math.tanh(3 - 6 * q_i)]
        sample_list.append(x_i)
    return sample_list


def get_hd_dataset(numOfSamples):
    sample_list = []
    coef = []
    for x in range(0, 5):
        one_set_coef = []
        for y in range(0, 5):
            one_set_coef.append(random.random())
        coef.append(one_set_coef)
    for x in range(0, numOfSamples):
        d_1 = random.random()
        d_2 = random.random()
        d_3 = random.random()
        d_4 = random.random()
        d_5 = random.random()
        powers = []
        for y in range(0, 5):
            one_set_pow = [pow(d_1, random.random()), pow(d_2, random.random()), pow(d_3, random.random()), pow(d_4, random.random()), pow(d_5, random.random())]
            powers.append(one_set_pow)

        x_i = (numpy.mat(coef + powers) * numpy.mat([[d_1], [d_2], [d_3], [d_4], [d_5]])).transpose()
        x_i = x_i.tolist()
        sample_list.append(x_i[0])
    return sample_list



