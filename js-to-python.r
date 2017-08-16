# Script to convert dictionary from js to Python
# Matthew Wolff (lover of regex)
# https://github.com/matthewwolff

words <- readLines("C:\\Users\\mmwolff\\Downloads\\library.txt")
words <- strsplit(words,"\"")
words <- lapply(words, function(x) paste(x[2],x[4], sep="\":\""))
words <- words[2:(length(words)-1)] # eliminate first and last lines (errors)
output <- ""
for(i in 1:length(words))
{
  if(i == 1)
  {
    output = c(output,"var lib = {\n")
  }
    
  if(i == length(words))
  {
    output <- c(output,paste("\"",words[[i]],"\"\n", sep=""))
    output <-  c(output, "}\n")    
  }
  else
    output <-  c(output,paste("\"",words[[i]],"\",\n", sep=""))
}
writeLines(output,"C:\\Users\\mmwolff\\Downloads\\minionLibrary.txt");head(output,10)
