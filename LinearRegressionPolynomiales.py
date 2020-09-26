from sklearn.preprocessing import PolynomialFeatures

reg = LinearRegression().fit(X_ploy, y)

line_poly = poly.transform(line)
plt.plot(line, reg.predict(line_poly), label ='polynomial linear regression')
plt.plot(X[:, 0], y, 'o', c='k')
plt.ylabel("Regression output")
plt.xlabel("Input feature")
plt.legend(loc="best")
