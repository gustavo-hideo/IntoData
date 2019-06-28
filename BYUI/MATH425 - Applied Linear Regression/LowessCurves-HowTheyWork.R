# Get some data for X and Y
X <- cars$speed
Y <- cars$dist

# Ensure the data has no missing values in any of the X,Y pairs
keep <- which(!is.na(X) & !is.na(Y))
X <- X[keep]
Y <- Y[keep]

# Decide on the fraction of points to use for the local regressions
f <- 1/2

# Identify the total sample size and sample size corresponding to f
n <- length(X) #total sample size
nn <- floor(n*f) #number of dots corresponding to percentage f

# Create storage for the lowess fitted-values
lfit <- rep(NA,n)

# Begin the for loop to compute lowess fitted-values
for (xc in 1:n){ #let each dot be the center dot, one at a time
  xdists <- X - X[xc]  #compute distance from all X-values to center dot x-value
  r <- sort(abs(xdists))[nn] #locate the nn"th" largest x-distance from center x-value
  xdists.nbrhd <- which(abs(xdists) < r) #identify x-values within the neighborhood
  w <- rep(0, length(xdists)) #initialize the weights for all x-values at 0
  w[xdists.nbrhd] <- (1 - abs(xdists[xdists.nbrhd]/r)^3)^3 #tri-cubic weight function 
  plot(Y ~ X, pch=21, bg=rgb(.53,.81,.92, w), #color dots by their weights
       col=rgb(.2,.2,.2,.3), cex=1.5, yaxt='n', xaxt='n', xlab="", ylab="")
  points(Y[xc] ~ X[xc], pch=16, col="orange") #add center dot to plot
  lmc <- lm(Y ~ X + I(X^2), weights=w) #run weighted regression
  curve(lmc$coef[1] + lmc$coef[2]*x + lmc$coef[3]*x^2, #draw line on neighborhood using from and to
        from=min(X[xdists.nbrhd]), to=max(X[xdists.nbrhd]), col="orange", add=TRUE)
  lines(lfit[1:xc] ~ X[1:xc], col="gray") #add lowess line up to current center dot
  
  #lines(lowess(X,Y), col=rgb(0.698,0.133,0.133,.2))
  cat("\n\n")
  readline(prompt=paste0("Center point is point #", xc, "... Press [enter] to continue..."))
  
  
  MADnotThereYet <- TRUE
  count <- 0
  while(MADnotThereYet){ #while loop will continue until "MadnotThereYet" becomes false
    
    readline(prompt=paste0("\n   Adjusting line to account for outliers in the y-direction... Press [enter] to continue..."))   
    
    # overwrite current regression to lighter color if new regression still needed:
    curve(lmc$coef[1] + lmc$coef[2]*x + lmc$coef[3]*x^2, from=min(X[xdists.nbrhd]), to=max(X[xdists.nbrhd]), col="wheat", add=TRUE)
    
    # update the weights
    MAD <- median(abs(lmc$res))
    resm <- lmc$res/(6*MAD)
    resm[resm>1] <- 1
    bisq <- (1-resm^2)^2
    w <- w*bisq
    obs <- coef(lmc)
    lmc <- lm(Y ~ X + I(X^2), weights=w)
    
    curve(lmc$coef[1] + lmc$coef[2]*x + lmc$coef[3]*x^2, from=min(X[xdists.nbrhd]), to=max(X[xdists.nbrhd]), col="orange", add=TRUE)
    
    #stopping criterion for the weighted regressions in y-direction
    count <- count + 1
    if ( (sum(abs(obs-lmc$coef))<.1) | (count > 3))
      MADnotThereYet <- FALSE
    
  }
  
  ########
  curve(lmc$coef[1] + lmc$coef[2]*x + lmc$coef[3]*x^2, from=min(X[xdists.nbrhd]), to=max(X[xdists.nbrhd]), col="green", add=TRUE)
  points(lmc$coef[1] + lmc$coef[2]*X[xc] ~ X[xc], pch=16, col="green")
  ########
  
  readline(prompt=paste0("\n   Use final line to get fitted value for this point... Press [enter] to continue to next point..."))
  
  lfit[xc] <- predict(lmc, data.frame(X=X[xc]))
  lines(lfit[1:xc] ~ I(X[1:xc]^2), col="gray")
  
  
  if (xc == n){
    readline(prompt=paste0("\n  Press [enter] to see actual Lowess curve..."))
    lines(lowess(X,Y, f=f), col="firebrick")
    legend("topleft", bty="n", legend="Actual lowess Curve using lowess(...)", col="firebrick", lty=1)
  }
  
  
}
