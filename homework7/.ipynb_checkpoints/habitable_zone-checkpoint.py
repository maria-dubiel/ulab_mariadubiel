# File: habitable_zone.py
#source for equations: https://www.planetarybiology.com/calculating_habitable_zone.html 
import numpy as np

def absolute_visual_magnitude(apparent_magnitude, distance):
    """
    This function will calculate the absolute visual magnitude of a star given apparent visual magnitude and distance in parsecs.
    
    Inputs:
    apparent_magnitude (float): apparent magnitude of the star (visual spectrum)
    distance (float): distance to the star from earth in parsecs

    Output:
    absolute_mag (float): absolute magnitude of the star
    """
    absolute_mag = apparent_magnitude - (5 * np.log10(distance/10))
    return absolute_mag

def bolometric_magnitude(absolute_mag, bolometric_correction_constant):
    """
    This function will calcualte the bolometric magnitude using the absolute magnitude and the bolometric correction constant
    
    Inputs:
    absolute_mag (float): absolute magnitude of the star
    bolometric_correct_constant (float)

    Output:
    bolometric_ mag (float): bolometric_magnitude of the star
    """
    bolometric_mag = absolute_mag + bolometric_correction_constant
    return bolometric_mag

def calculate_abs_luminosity(bolometric_mag):
    """
    This function will calcualte the absolute luminosity of the host star using the bolometric magnitude
    
    Inputs:
    bolometric_ mag (float): bolometric_magnitude of the star

    Output:
    absolute_luminosity (float): the absolute luminosity of the host star in terms of the absolute luminosity of the sun
    """
    absolute_luminosity = 10 * ((bolometric_mag - 4.72) / -2.5)
    return absolute_luminosity

def inner_boundary(absolute_luminosity):
    """
    This function will find the inner boundary of the habitable zone of the star using the absolute luminosity

    Inputs:
    absolute_luminosity (float): the absolute luminosity of the host star in terms of the absolute luminosity of the sun

    Output:
    inner_bound (float): the inner boundary of the habitable zone in astronomical units (AU)
    """
    inner_bound = (absolute_luminosity / 1.1) ** 0.5
    test = 5
    return inner_bound

def outer_boundary(absolute_luminosity):
    """
    This function will find the outer boundary of the habitable zone of the star using the absolute luminosity

    Inputs:
    absolute_luminosity (float): the absolute luminosity of the host star in terms of the absolute luminosity of the sun

    Output:
    outer_bound (float): the outer boundary of the habitable zone in astronomical units (AU)
    """
    outer_bound = (absolute_luminosity / 0.53) ** 0.5
    return outer_bound

def is_it_in_habitable_zone(planet_distance_arr, inner_bound, outer_bound):
    """
    This function will take in a multidimensional array with the distance measurements of several planets, take the mean of the measurments for each planet and then return how many planets are otuside the habitable zone and how many are inside
    Inputs: 
    inner_bound (float): the inner boundary of the habitable zone in astronomical units (AU)
    outer_bound (float): the outer boundary of the habitable zone in astronomical units (AU)
    planet_distance_arr (arraY): ([
    [a, b, c, d], <- measurments for planet 1
    [e, f, g, h]]) <- measurments for planet 2

    Outputs: 
    "Planet is too close!", "Planet is in habitable zone!!", "Planet is too far!" (depending on where the planet is)
    "Number of planets in habitable zone:{planets_in_habitable_zone}, Number of planets outside habitable zone:{planets_outside_habitable_zone}"
    """
    planets_in_habitable_zone = 0
    planets_outside_habitable_zone = 0
    avg_planet_distances = np.mean(planet_distance_arr, axis=1)
    for j in avg_planet_distances:
            if j < inner_bound:
                planets_outside_habitable_zone += 1
                print("Planet is too close!")
            elif inner_bound <= j <= outer_bound:
                planets_in_habitable_zone += 1
                print("Planet is in habitable zone!!")
            else:
                planets_outside_habitable_zone += 1
                print("Planet is too far!")
    return(f"Number of planets in habitable zone:{planets_in_habitable_zone}, Number of planets outside habitable zone:{planets_outside_habitable_zone}")








