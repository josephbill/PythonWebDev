## PYTHON FUNDAMENTALS
## BASIC SYNTAX AND STRUCTURE 
 - Indentation : python uses this concept to define block of code 
 - Variables :Python variables are dynamically typed , storing reference
 - Print statement : uses to log out information 
 - Data types : nature/type of data

## Data types 
- Numbers : Integer (int) , Floating Point(float) , Complex (complex => bigger than int)
- Strings : Text data , 'Joseph' , "Joseph"
    Python sequences
- Lists : Ordered , mutable(can be changed) collections of items.
- Tuples : Ordered, immutable(cannot be changed) collections of items. 
- Dictionaries : Unordered, mutable collections of key and value pairs.
- Boolean : These values evaluate to True or False
- None : nil 

## Operators 
 - Arithmetic Operators : +,-,*,/,//(floor division), %(modulo) , **  
 - Comparison Operators : result of comparison is always true or false
== : equal to , != : is not equal , < , > , <= : less than or equal to , >= greater than equal to
 - Logical Operators : and && : whats on the left and right must be true or must false
                       or : only one aspect has to be true or match 
                       not : opposite of the value 

## Control Flows 
- Conditionals : if, elif, else for decision-making
- Loops : Iterate of sequences : to process every single element in a collection 
          repetition of tasks

## Function 
- a block of code that will execute and return a value


- functions, variables , primitive data types (strings, numbers, booleans, none)





### Computational thinking 
- algorithm development 
- algorithm : step-by-step process that will lead to an output i.e. the solution 
- DECOMPOSITION : BREAKDOWN OF A COMPLEX PROBLEM INTO A SUBSET OF PROBLEMS 

### loopS
loops are used to execute a block of code : repeatedly 
two main types of loops 
- for loop
- while loop 

## for loop 
- the for loop is used to iterate over a sequence (ordered types of sequences : list, tuple, string or range)
- used when we know the number of iterations needed 
- x  = [ 1,2,3,5,5,6,7 ]  : size/length of the sequence : 7
-                          : index position starts from 0

x = (1,2,3,4,5,6,7 ) : size/length of the sequence : 7 
                      : for the index start of 0

x is a list : len(x)

## while loop 
is used to repeat a block of code as long as a given condition is true 
when we don't know how many iterations are needed 

## Loop statements 
break : exists the loop prematurely 
continue : skips the current iteration and proceeds with the next iteration

## nested loops 
use loops inside loops 
[[] , [] , []]
very useful when operating on multi-dimensional data structures ( sequences )

 


## sequences coverage (LISTS < TUPLES < DICTIONARIES < SETS)
1. Identify the sequence : syntax 
2. Ordering of elements in the sequence : 
If ordered the reference is in index position
x = [1,2,3,4,5,"apple", True]
If unordered the reference is through keys : Dictionaries/ Objects
{
  7 : "1"
}
3. Access of the elements 
4. Looping : how do you loop the sequence 
5. Inbuilt operations : del(0) , len(x)  .append 


### Object Oriented Programming 
OOP is a programming paradigm that uses objects and classes to structure and organize code 
- Allow modularization 
- Allow Reusability 
- Allow Scalability

### Class : 
A blueprint for creating objects (instances)
A class will define , attributes(data) and methods(functions) thats the object will have

### Object :
An instance of a class 

# string : everything is an object 

Car (attributes)  : Class 
 - color , model , registration , yom , wheels , size , transmission


## Principles of OOP 
 - Inheritance : allows classes to inherit attributes and methods from another class 
 - Encapsulation : bundling of data and methods that operate on the data within a class
 - Polymorphism  : means many forms and is used to perform a single action in different ways
 - Abstraction : exposing what is only essential

## Object Relationships 
Defining how different object can interact with one another 
Common types relationships amongst objects 
1. Association
Description : A general relationship where one object uses another. Often described as a 'has a' relationship
One object can hold reference to another

Scenario 
- Libraries and books : A lib has many books , but books can exist independently of a lib
- Customer and orders : customer can place orders , and orders can be linked to a specific customer 

2. Aggregation 
Description : A specific type of association that represents a 'whole-part' relationship, where one part can exist independently of the
whole 

Scenario 
- Team and player : a team can consist of multiple players but players can still exist without the team
- Libraries and books : A lib has many books , but books can exist independently of a lib
- School and teachers

3. Composition 
A stronger form of aggregation , the 'whole' owns the 'part' , the parts lifecycle is dependent on the whole. If the whole is destroyed 
the parts are also destroyed 

Scenario 
- House and Room : A house consist of rooms if the house is demolished the rooms no longer exist 
- Car and Engine : 
- Payroll and Employee : 

4. Inheritance 
A relationship where one class inherits the properties and behaviour of another class , "is-a" relationship

5. Dependency 
One object relies on another to perform its function. "uses-a" relationship , one class uses another but does not own it

   
### SQL : Structured Query Language 
the standard language for interacting with relational databases 
1. Manage and manipulate data stored in tables 
2. SQL supports the CRUD operations 
3. Lightweight

## RDBMS : SQlite 
-Sqlite is a lightweight , serverless SQL database engine : great for small applications , 
offline apps, or development use
- Stores data in a single file. : making it easy for set up and access by code without a
separate database server









