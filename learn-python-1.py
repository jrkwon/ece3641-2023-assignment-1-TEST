# %% [markdown]
# # Hello, World!

# %% [markdown]
# Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program without boilerplate (prepared) code. The simplest directive in Python is the `print` directive - it simply prints out a line (and also includes a newline, unlike in C).

# %% [markdown]
# To print a string in Python 3, just write:

# %%
print("This line will be printed.")

# %%
x = True
if x is False:
    print('x is False')
else:
    print('x is True')


# %% [markdown]
# # Variables and Types

# %% [markdown]
# Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in 
# Python is an object.
# 
# This tutorial will go over a few basic types of variables.
# 
# ## Numbers

# %%
# integers
myint = 7
print('myint is ', myint)

# floats
myfloat = 7.7
print(myfloat)

# %% [markdown]
# ## Strings
# Strings are defined either with a single quote or a double quotes.
# 

# %%
str = 'hello'
print(str)

str = "hello"
print(str)


