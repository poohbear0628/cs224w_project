Clustering Coefficient Analysis
================
Samuel Hansen

What is the relationship between clustering coefficient and negative sentiment?
===============================================================================

Complete Graph
--------------

We can examine whether a relationship exists between the weighted clustering coefficient and negative sentiment by examining the following plot and inspecting a linear regression analysis.

``` r
complete_top_10_df %>%
  ggplot(mapping = aes(x = clust_coef, y = posemo)) +
  geom_point() +
  geom_smooth(method = "loess") +
  labs(x = "Weighted Clustering Coefficient", 
       y = "Negative Emotion Score",
       title = "Complete Graph: \nClustering Coefficient vs. Negative Sentiment") 
```

    ## Warning: Removed 7 rows containing non-finite values (stat_smooth).

    ## Warning: Removed 7 rows containing missing values (geom_point).

![](clust_coef_analysis_files/figure-markdown_github/unnamed-chunk-2-1.png)

``` r
lm.fit <- lm(negemo ~ clust_coef, data = complete_df)
summary(lm.fit)
```

    ## 
    ## Call:
    ## lm(formula = negemo ~ clust_coef, data = complete_df)
    ## 
    ## Residuals:
    ##       Min        1Q    Median        3Q       Max 
    ## -0.015161 -0.004759 -0.000667  0.003979  0.110055 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  0.0193548  0.0007355  26.316   <2e-16 ***
    ## clust_coef  -0.0001874  0.0010487  -0.179    0.858    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 0.006638 on 2046 degrees of freedom
    ## Multiple R-squared:  1.561e-05,  Adjusted R-squared:  -0.0004731 
    ## F-statistic: 0.03194 on 1 and 2046 DF,  p-value: 0.8582

There appears to be a **no** statistically significant relationship between clustering coefficient and negative sentiment.

Complete Graph Filtered to Top 10% of Edge Weights
--------------------------------------------------

We can examine whether a relationship exists between the weighted clustering coefficient and negative sentiment by examining the following plot and inspecting a linear regression analysis.

``` r
complete_top_10_df %>%
  ggplot(mapping = aes(x = clust_coef, y = posemo)) +
  geom_point() +
  geom_smooth(method = "loess") +
  labs(x = "Weighted Clustering Coefficient", 
       y = "Negative Emotion Score",
       title = "Complete Top 10% Graph: \nClustering Coefficient vs. Negative Sentiment") 
```

    ## Warning: Removed 7 rows containing non-finite values (stat_smooth).

    ## Warning: Removed 7 rows containing missing values (geom_point).

![](clust_coef_analysis_files/figure-markdown_github/unnamed-chunk-4-1.png)

``` r
lm.fit <- lm(negemo ~ clust_coef, data = complete_top_10_df)
summary(lm.fit)
```

    ## 
    ## Call:
    ## lm(formula = negemo ~ clust_coef, data = complete_top_10_df)
    ## 
    ## Residuals:
    ##       Min        1Q    Median        3Q       Max 
    ## -0.015462 -0.004725 -0.000644  0.003963  0.109668 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  0.0202158  0.0004896  41.287   <2e-16 ***
    ## clust_coef  -0.0019582  0.0009336  -2.097   0.0361 *  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 0.006639 on 2039 degrees of freedom
    ##   (7 observations deleted due to missingness)
    ## Multiple R-squared:  0.002153,   Adjusted R-squared:  0.001664 
    ## F-statistic: 4.399 on 1 and 2039 DF,  p-value: 0.03608

There appears to be a weak, yet statistically significant relationship between clustering coefficient and negative sentiment.

``` r
# IGNORE THIS CODE FOR NOW 
# df <-
#   df %>%
#   mutate(quartile = ifelse(clust_coef <= quantile(clust_coef, prob = .25, na.rm = T), 
#                            "bottom_25",
#                            ifelse(clust_coef >= quantile(clust_coef, prob = .75, na.rm = T), 
#                                   "top_25", "middle")))
# df %>%
#   filter(quartile != "middle") %>%
#   ggplot(mapping = aes(x = quartile, y = negemo)) +
#   geom_bar(stat = "identity") +
#   labs(x = "Weighted Clustering Coefficient Quartile",
#        y = "Negative Sentiment Score",
#        title = "Negative Sentiment vs. Top & Bottom Clustering Coefficient Quartiles")
```
