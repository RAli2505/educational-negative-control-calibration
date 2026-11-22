# Binary-risk conditions and limits of oriented pooling

This note gives explicit results for a restricted structural model. The algebra, triangle inequality and Hoeffding argument are standard; no priority claim is made. Independent samples here mean a training/evaluation split, not identification of transport between different populations.

## 1. Model, estimand and observed contrast

Let Z be finitely many observed strata with population probabilities p_z, U a bounded d-dimensional latent vector, A a binary exposure, Y a binary outcome and C_1,...,C_K binary candidate controls. Assume consistency and assignment independent of the potential-response errors conditional on (Z,U). Suppose

    E[Y(a)|z,u] = m(z) + tau(z)*a + lambda_Y(z)'u,
    E[C_k(a)|z,u] = c_k(z) + gamma_k(z)*a + lambda_k(z)'u.

Every conditional mean must lie in [0,1]. A valid control has gamma_k(z)=0. This is an additive probability model, not a logistic model; binary outcomes do not by themselves imply equal loadings. The target is population ATE theta=sum_z p_z tau(z).

Define Delta(z)=E[U|A=1,z]-E[U|A=0,z]. Standardized observed contrasts are

    d_Y = theta + sum_z p_z lambda_Y(z)'Delta(z),
    d_k = sum_z p_z {gamma_k(z)+lambda_k(z)'Delta(z)}.

The second equality separates exclusion from bias comparability. The controls can have gamma=0 and still fail as measurements of target bias.

## 2. Bias of the original correction

Condition on an independent training sample D. Let signs s_k(D) be +/-1 and weights w_k(D)>=0 sum to one. The retained procedure has equal weights 1/K. Define q_s=d_Y-sum_k w_k s_k d_k. Then

    q_s-theta = sum_z p_z [(lambda_Y(z)-sum_k w_k s_k lambda_k(z))'Delta(z)
                           -sum_k w_k s_k gamma_k(z)].                         (1)

Proof: substitute the two observed-contrast identities and collect terms. Assignment exchangeability given (Z,U), the additive model and consistency justify each observed-contrast identity by conditional expectation. No exchangeability given Z alone is assumed.

In the one-factor, correct-orientation, valid-control case with constant loadings, equation (1) becomes (lambda_Y-mean_k |lambda_k|)*Delta. Sign alignment removes cancellation between controls, but it does not identify lambda_Y or force it to equal the mean control loading.

The population bias-squared improvement is 2*B*M-M^2, with B=d_Y-theta and M=sum w*s*d_k. Thus, when B!=0 and sampling error is negligible, improvement requires 0<M/B<2. At finite n the exact condition is 2*B*mu-mu^2-Var(C)+2*Cov(T,C)>0 for the full random correction C and uncorrected T, where mu=E[C]. This identity also includes randomness of training signs. Neither identity is a new causal-identification theorem.

## 3. A substantive mismatch allowance

Suppose scientific information provides, for every z and coordinate j,

    |lambda_Y,j(z)-sum_k w_k s_k lambda_k,j(z)| <= epsilon_j(z),
    |Delta_j(z)| <= D_j(z),    |gamma_k(z)| <= Gamma_k(z).

Then equation (1) and the triangle inequality give

    |q_s-theta| <= R_s
      := sum_z p_z [sum_j epsilon_j(z)*D_j(z)+sum_k w_k Gamma_k(z)].       (2)

There is no claim that epsilon, D or Gamma are identified by the control estimates. They are restrictions on the risk surface, treatment selection and control validity. Example interpretation: epsilon=.03 for a scalar U in [-1,1] restricts the target/control difference in the change of risk across the full U range to at most .06, not .03. These restrictions require subject-matter support, external validation or an explicitly labelled sensitivity grid.

If approximate matching holds for a correct reference orientation s*, but the estimated orientation is s, a sufficient coordinatewise allowance is

    epsilon_j(z) + 2*sum_{k:s_k!=s*_k} w_k*L_kj(z),

where |lambda_kj(z)|<=L_kj(z). This follows by adding and subtracting the correctly oriented pool. Weak proxy evidence cannot justify deleting this additional term. Allowing every sign combination is conservative but needs no successful sign selection. If weights are learned in training, the restriction must hold for the actual selected weights or uniformly over possible training selections.

The benchmark also calculates a sharper bound using the true simulated loadings, Delta and gamma. That value is labelled **oracle structural bound**. Its evaluation checks the mathematical statement; it is not a data-driven solution to the editor's concern.

## 4. Finite-sample conditional interval with known marginal propensity

Assume training is independent of n iid evaluation observations from the target population; e(z)=P(A=1|Z=z) is known and eta<=e(z)<=1-eta for a fixed eta>0. Freeze the training signs and weights. Set

    V_i = Y_i-sum_k w_k s_k C_ik,
    H_i = A_i V_i/e(Z_i) - (1-A_i)V_i/{1-e(Z_i)},
    M_s = 1+sum_{k:s_k=-1}w_k,
    r_n = (2*M_s/eta)*sqrt{log(2/alpha)/(2*n)}.

Conditional on training, E[H_i|D]=q_s. Since Y,C are binary and weights lie on the simplex, -sum_{s=+1}w_k <= V <= 1+sum_{s=-1}w_k, so |V|<=M_s and H lies in [-M_s/eta,M_s/eta]. Hoeffding's inequality yields

    P(|mean(H)-q_s|>r_n | D) <= alpha.

Consequently, if a training-measurable R_s satisfies (2) almost surely,

    I(D) = [mean(H)-r_n-R_s, mean(H)+r_n+R_s] intersect [-1,1]             (3)

contains theta with probability at least 1-alpha, conditionally on D and hence unconditionally. The benchmark leaves intervals untruncated to compare their raw widths. Truncation to the binary-ATE parameter space preserves coverage. Proof: on the Hoeffding event, |mean(H)-theta|<=r_n+R_s by the triangle inequality; theta is itself in [-1,1].

If the structural restriction holds only on a training event of probability >=1-beta, the same union-bound argument gives >=1-alpha-beta unconditional coverage. No theorem here estimates beta from a weak proxy.

This result allows estimated training signs and simplex weights, but the benchmark retains equal weights. It **does not** justify the historical MoM interval, an estimated-propensity AIPW interval on OULAD/XES, same-sample sign selection, unknown structural allowances, or transport between populations. Known e(Z) is a simulation design input; this is not a randomized treatment because hidden U still affects A.

For comparison the benchmark adds prespecified R values to a covariance-aware Wald interval. These are sensitivity displays, asymptotic sampling approximations, and not instances of the finite-sample theorem above. More width alone is not improved estimation efficiency.

## 5. Why original summaries cannot determine the causal correction

Consider no Z, U equally likely +/-1, P(A=1|U)=.5+.15*U, and six controls E[C_k|U]=.5+.14*s_k*U with alternating s_k. Let G=U+independent noise. For the target use E[Y(a)|U]=.5+tau*(a-.5)+lambda*U. Two admissible models are

    Model A: tau=0,     lambda=.14;
    Model B: tau=.042,  lambda=.07.

Both have d_Y=tau+.60*lambda=.084; every correctly oriented control contrast is .084. Target/control marginal risks are .5, their marginal treatment contrasts agree, their marginal arm variances agree, and the proxy orientation signs agree (positive for Y). Hence the original population MoM point correction is zero in both models, although their ATEs differ by .042. This is equivalence of the summaries retained by that procedure, not observational equivalence of the complete joint distribution: target/control cross-covariances can differ. It proves the limited point that sign alignment plus those summaries does not by itself identify the target effect.

## 6. Relation to existing work and permissible contribution

COCA, single-proxy identification, equi-confounding, multi-outcome factor sensitivity and bias-aware intervals already address related identification questions. Equation (3) is a direct application of established concentration and sensitivity reasoning, not an asserted improvement over these methods. The new material contributes a clearly specified binary educational benchmark, independent sign estimation, decomposition of several failures, and an explicit separation of oracle coverage from feasible diagnostic checks. Establishing a new methodological result would still require an identified information advantage, weaker necessary assumptions or sharper valid inference compared with the closest applicable methods.
