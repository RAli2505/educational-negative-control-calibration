# Prospective local experiment specification

Written after the earlier editorial audit and before executing this extension. This is not an external preregistration. All scenarios and adverse results will be retained.

## Goal and scope

Retain the original equal-pool sign correction. Determine when its error reduction is caused by correct orientation and when it fails because control bias does not match target bias. Produce an empirical contribution, an explicit binary-risk structural analysis, and a targeted prior-art comparison. No claim of a new identification method or universally superior estimator is authorized by the experiment design.

## Data-generating model

Binary treatment A, binary target Y, six binary candidate controls, three observed strata Z, two bounded latent coordinates U. Assignment is e(Z)+kappa*(U1-E[U1|Z]), with e=(.35,.50,.65). Conditional target probability is .45+.05*(Z-1)+tau*A+lambdaY'U. Controls have conditional probabilities .50+b_k*(Z-1)+gamma_k*A+lambda_k'U. Every probability is checked, never silently clipped. All random response errors are independent conditional on A,Z,U. tau is 0 or .08, hence the population ATE is exactly known.

Synthetic U consists of independent symmetric +/-1 coordinates, independent of uniformly distributed Z. In the OULAD-profile experiment, the empirical joint distribution of credits strata, age and previous attempts replaces this distribution; treatment, proxy, target and controls are all generated. This is not evidence of a known effect on real retention.

The empirical population is constructed only from archived OULAD training registrations, deterministically deduplicated by student. Credits define Z (<60, 60--119, >=120). U1 codes age 0--35=-1, 35--55=.4, 55+=1; U2 codes any previous attempts as +/-1. This coding is a simulation choice, not a validated latent educational construct. Evaluation rows are independent draws with replacement from this fixed population. Record file hashes and aggregate counts, never release individual records.

Proxy G=rho*standardized(U1)+sqrt(1-rho^2)*Normal(0,1), with rho in {0,.25,.75}; this is a coefficient, not necessarily its observed marginal correlation in the OULAD population. A stress scenario adds 2*(Z-1) to G and negative stratum trends to controls. Orientation uses a separate training sample (n=1000). Evaluation uses n=2000 unless specified. The training stage is re-generated in every replication.

## Scenarios and analysis

- Synthetic grid: control loading scale {.25,.5,1,1.5,2} x proxy {0,.25,.75} x tau {0,.08}: 30 cells.
- Structural stresses at rho=.75, scale=1: second-factor controls, opposed confounding factors, one invalid control, two invalid controls, observed-stratum sign reversal; tau {0,.08}: 10 cells.
- OULAD-profile: scale {.5,1,2} x proxy {.25,.75} x tau {0,.08}: 12 cells.
- Sample-size stresses: matched scale=1, rho=.25, n {500,8000}, tau {0,.08}: 4 cells.
- No-confounding reference: kappa=0, rho=.75, tau {0,.08}: 2 cells.

Total 58 cells, 1000 replications each; one fixed seed, common random numbers across scenarios. No scenario removal for poor performance. An empty treatment-by-stratum cell is a recorded failure, not an invitation to redraw. Three observed strata allow saturated standardization with a common adjustment design for every outcome. Known population stratum weights are used. Joint influence scores provide covariance-aware standard errors. This differs from the earlier cross-fit machine-learning audit and is explicitly a structural benchmark.

Point comparators: uncorrected; unsigned equal-pool; original raw-correlation sign pool; residual-correlation sign pool (ablation, not claimed new); true-loading sign pool (oracle ablation); oriented median (point comparator only); and IPW with the full hidden assignment probability (oracle benchmark, unavailable to an analyst). The MoM interval and shared-score Wald interval are evaluated separately. The median is not represented as a replication of NC-DiD or COCA.

Sensitivity comparisons: prespecified residual-bias allowances R={0,.025,.05,.10,.20} added to the shared-score interval. Separately evaluate a finite-sample Hoeffding interval for known marginal propensity, independent training orientation, and a DGP-computed structural bias bound. Label this last bound oracle: it cannot be estimated from the observed control panel alone. Do not apply its theorem to estimated-propensity real-data AIPW.

Outcomes: bias, RMSE, coverage, rejection probability (type I under tau=0; power otherwise), interval width, paired MSE difference with Monte Carlo uncertainty, orientation-error rate, structural bias-bound violation and nuisance-cell failure count. Report every cell in machine-readable form. Do not select an optimal method using evaluation truth and then report it as feasible.

## Evidence and novelty boundary

Add a theoretical explanation of summary-level nonidentification, an exact bias decomposition and a finite-sample conditional coverage result under stated information. These are elementary consequences of established bias-aware inference, not asserted novel theorems. The candidate substantive contribution is the educational benchmark and a documented explanation of failure modes. Compare explicitly with COCA, empirical calibration, factor-outcome sensitivity analysis, NC-DiD, and the 2026 distributional-calibration preprint. A free methodological gap remains unconfirmed.

Existing manuscript and abstract remain unchanged in this run. Deliver a standalone, article-ready supplement and a Russian interpretation rather than silently rewriting the previously reviewed claims.
