function b = spdiag(a)
a = a(:);
n = length(a);
b = sparse(1:n, 1:n, a, n, n, n);
end