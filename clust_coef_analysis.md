Clustering Coefficient Analysis
================
Samuel Hansen

What is the relationship between clustering coefficient and negative sentiment?
===============================================================================

We can examine whether a relationship exists between the weighted clustering coefficient and negative sentiment by examining the following plot and inspecting a linear regression analysis.

``` r
df %>%
  ggplot(mapping = aes(x = clust_coef, y = posemo)) +
  geom_point() +
  geom_smooth(method = "loess") +
  labs(x = "Weighted Clustering Coefficient", 
       y = "Negative Emotion Score",
       title = "Clustering Coefficient vs. Negative Sentiment") 
```

    ## Warning: Removed 7 rows containing non-finite values (stat_smooth).

    ## Warning: Removed 7 rows containing missing values (geom_point).

![](clust_coef_analysis_files/figure-markdown_github/unnamed-chunk-2-1.png)

``` r
lm.fit <- lm(negemo ~ clust_coef, data = df)
summary(lm.fit)
```

    ## 
    ## Call:
    ## lm(formula = negemo ~ clust_coef, data = df)
    ## 
    ## Residuals:
    ##       Min        1Q    Median        3Q       Max 
    ## -0.015431 -0.004726 -0.000648  0.003952  0.109668 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  0.0201854  0.0003728   54.15  < 2e-16 ***
    ## clust_coef  -0.0037080  0.0013384   -2.77  0.00565 ** 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 0.006634 on 2039 degrees of freedom
    ##   (7 observations deleted due to missingness)
    ## Multiple R-squared:  0.00375,    Adjusted R-squared:  0.003262 
    ## F-statistic: 7.675 on 1 and 2039 DF,  p-value: 0.005649

There appears to be a weak, yet statistically significant relationship between clustering coefficient and negative sentiment.
