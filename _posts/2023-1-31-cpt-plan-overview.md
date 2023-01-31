---
toc: true
layout: post
description: "My Collegeboard Creat Perfomance Task Submission Plan"
categories: [markdown]
title: CPT Overview
permalink: /cptplan
---

# Overview

My job in Team ReciPies will be to create the recipe suggester, with which the user selects dietary restrictions or certain preferances, and is then given recipe suggestions to cook.

# Purpose and Function

The purpose is to provide customers a place to get different types of recipes filtered by the user's preferences.

​Function: The frontend will have checkboxes for the users to select common dietary restrictions, and a submit button. When the submit button is clicked it will send the user's preferences to the backend which will recommend a few recipes not containing those ingredients.

# Data Abstraction

The data/user preferences will be sent through a JSON file.

# Managing Complexity

Using our API, we will easily be able to sort through the recipes and see which ones do and do not contain the user's allergens. 

# Procedural Abstraction

I will use a procedure to see if the randomly selected recipe given by the API has any of the ingredients that the user doesn't want. If they do, I will redo the procedure until it gives a few recipes that the user can eat.

# Algorithmic Implementation

I will use sequencing to sort the recipes by the user reviews, as the ones with highest reviews should be recommended first.

# Testing / Video Plan

I will have 2 different test cases with completely different preferences to show how it will suggest totally different recipes that don't contain those ingredients.

