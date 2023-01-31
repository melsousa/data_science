# vetor e gráfico básico
x = c(12,34,56,79)
y = c(1,6,9,14)
plot(x,y)

install.packages("e1071")
library(e1071)

#descarregar pacote
detach("package:e1071", unload=TRUE)

#remover
remove.packages("e1071")

#vetores de outro tipos
y = c("a", "b", "c")
y
X = c(1L,2L,3L)
x

#matrizes
VADeaths
colnames(VADeaths)
rownames(VADeaths)

#DATA frame
longley
longley[,1:3]
longley$Unemployed

#listas
ability.cov
ability.cov$cov
ability.cov[1]
class(ability.cov$cov)
class(ability.cov$center)

#fatores
state.region
