A code that compute the number of labeled semisimple ring with p^n elements.

A labeled semisimple ring with k elements is the data of a semisimple ring structure on the set {1,...,k}. 
Hence it is given by the disjoint union over isomorphism classes of semisimple ring with k elements R of the bijection of {1,...,k} to R, quotiented by the ring automorphisms of R.

Using the Artin-Wedderburn theorem, a finite semisimple ring is a product of matrix algebras over finite field. Moreover, this decomposition is canonical up to permutation of the isomorphic factors.
This allows to show that labeled semisimple ring with a×b elements with a and b relatively prime is the same as an permutation of {1,...,a×b} together with a labeled semisimple ring with a elements up to a permutation, and a labeled semisimple ring with b elements up to a permutation.
More simply, if we denote by u(n) the number of labeled semisimple ring with n elements, we have that if a and b are relatively prime, then:
u(a×b)=(a×b)!u(a)u(b)/(a!b!)

From this we see that computing u(p^n) is enough to compute the whole sequence.

How to compute u(p^n)?

By the Artin-Wedderburn theorem, a semi-simple ring with p^n elements is a product of matrix algebras of finite extension of F_p (with F_p the field with p elements):
R=M_{a_1}(F_{p^{b_1}})×M_{a_2}(F_{p^{b_2}})×...×M_{a_k}(F_{p^{b_k}})
Moreover, we have:
n=(a_1)²b_1+(a_2)²b_2+...+(a_k)²b_k

Hence we start by getting a partition of n. Then, for each term of the partition, we write it a²×b. Then we need to eliminate the duplicates.
Finally, we get a semisimple ring R and we need to compute its automorphism group. It is the product of the automorphism groups of its component times the permutation group of the isomorphic components.
We have a formula for the automorphism group of a matrix algebra. We compute the multiplicity of each term and we multiply by the according factorial numbers.

We can now do the sum on isomorphism class of semisimple ring with p^n elements R of (p^n)! over the cardinal of the automorphism group of R that we just computed.

(Sorry for the typos.)
