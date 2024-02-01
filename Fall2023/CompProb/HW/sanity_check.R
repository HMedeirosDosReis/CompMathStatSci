# Define the probability density function f(x)
pdf <- function(x) (1/36) * x * exp(-x/6)

# Define the moment generating function M_X(t)
moment_generating_function <- function(t, upper_limit) {
  integrand <- function(x) exp(t * x) * pdf(x)
  expected_value <- integrate(integrand, lower = 0, upper = upper_limit)$value
  return(expected_value)
}

# Choose a range of values for t to evaluate M_X(t)
t_values <- seq(-10, 1/6, by = 0.1)

# Set a sufficiently large upper limit for integration
upper_limit <- 100

# Calculate M_X(t) for each t
mgf_values <- sapply(t_values, moment_generating_function, upper_limit = upper_limit)

# Plot the moment generating function
plot(t_values, mgf_values, type = "l", 
     xlab = "t", ylab = "M_X(t)", 
     main = "Moment Generating Function")
##################

# Define the probability density function f(x)
pdf <- function(x) (1/36) * x * exp(-x/6)

# Calculate the mean (expected value) of X
mean_value <- integrate(function(x) x * pdf(x), lower = 0, upper = Inf)$value

# Calculate the second moment (E[X^2]) of X
second_moment <- integrate(function(x) x^2 * pdf(x), lower = 0, upper = Inf)$value

# Calculate the variance of X as Var(X) = E[X^2] - (E[X])^2
variance <- second_moment - mean_value^2

# Print the variance
cat("Variance of X =", variance, "\n")
