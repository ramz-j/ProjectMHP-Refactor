from problems.problem import *
from stats.basic_stats import BasicStats
# from state.solution import * 
from algorithms.genetic_algorithm import *
from algorithms.simulated_annealing import *
from algorithms.differential_evolution import *
from algorithms.harmony_search import *
from algorithms.cross_entropy import *
from algorithms.cooperative_cross_entropy import *
from algorithms.fireworks_algorithm import *
from algorithms.cooperative_search import *
from algorithms.random_walk import *

from datetime import datetime, date, time, timedelta
import calendar


class Agent(object):

	""" 
	:version:
	:author:
	"""


	""" ATTRIBUTES  
	problem  (public) 
	internal  (public) 
	nameMetaheuristic  (public) 
	paramMetaheuristic  (public) 
	nEvals  (public) 
	nExperim  (public) 
	info  (public) 
	algorithm  (public) 
	"""


	def __init__(self, problem, args):
		""" 
		@return  :
		@author
		"""
		self.problem = problem 
		self.metaheuristic = args[0] 
		self.paraMetaheuristic = args[1]
		self.nEvals = args[2]
		self.nExperim = args[3]
		self.stats = BasicStats(self.problem.typeProblem)
		self.objMetaheuristic = None   
		self.allsolutions = []
 

	def printFile(self):
		"""
		@return  :
		@author
		"""
		ahora = datetime.now()                     
		
		auxFile = "./output/"+ problem.nameShort+" "+ahora.day+"_" +(ahora.month)+"_"+ahora.year+" "+ahora.hour+"_"+ahora.minute+".txt"
		f = open (auxFile,'w')
		f.write(self.stats.toString())
		f.close()
 

	def init(self):
		"""
		@return  :
		@author
		"""
     
		self.problem.counter = Counter(self.nEvals) 
		self.stats.setLabel(self.metaheuristic +"---"+self.paraMetaheuristic+"["+str(self.nEvals)+"]");

		print("\n Experiments to "+self.metaheuristic)
		for e in range(self.nExperim):
			
			if (e % 15 == 14):
				print(" "+str(e)+"\n")
			else :
				print(" "+str(e))

			if (self.metaheuristic == "GA") :
				GA = GeneticAlgorithm(self.problem, self.paraMetaheuristic) 
				self.stats.add(GA.status.stateFinal)   
				
			if (self.metaheuristic == "SA") :
				SA = SimulatedAnnealing(self.problem, self.paraMetaheuristic) 
				self.stats.add(SA.status.stateFinal) 
				
			if (self.metaheuristic == "DE") :
				DE = DifferentialEvolution(self.problem, self.paraMetaheuristic) 
				self.stats.add(DE.status.stateFinal) 
                
			if (self.metaheuristic == "HS") :
				HS = HarmonySearch(self.problem, self.paraMetaheuristic) 
				self.stats.add(HS.status.stateFinal) 
                
			if (self.metaheuristic == "CE") :
				CE = CrossEntropy(self.problem, self.paraMetaheuristic) 
				self.stats.add(CE.status.stateFinal) 
                
			if (self.metaheuristic == "CCE") :
				CCE = CooperativeCrossEntropy(self.problem, self.paraMetaheuristic) 
				self.stats.add(CCE.status.stateFinal)
				                
			if (self.metaheuristic == "FWA") :
				FWA = FireworksAlgorithm(self.problem, self.paraMetaheuristic) 
				self.stats.add(FWA.status.stateFinal) 
                
			if (self.metaheuristic == "CooS") :
				CooS = CooperativeSearch(self.problem, self.paraMetaheuristic) 
				self.stats.add(CooS.status.stateFinal)     
                
			if (self.metaheuristic == "RW") :
				RW = RandomWalk(self.problem, self.paraMetaheuristic) 
				self.stats.add(RW.status.stateFinal) 
				self.allsolutions = RW.solutions # Revisar la inclusión de esta variable
												
			self.problem.counter = Counter(self.nEvals)  
		
		print("\n") 
		self.stats.prints();
		print("") 
		self.stats.printAllSolutions();


	def init2(self):
		"""
		@return  :
		@author
		"""
     
		# self.problem.counter = Counter(self.nEvals) 
		self.stats.setLabel(self.metaheuristic +"---"+self.paraMetaheuristic+"["+str(self.nEvals)+"]");

		print("\n Experiments to "+self.metaheuristic) 
		
		if (self.metaheuristic == "GA") :
			self.objMetaheuristic = GeneticAlgorithm(self.problem, self.paraMetaheuristic, False) 
            # self.stats.add(GA.status.stateFinal)   
				
		if (self.metaheuristic == "SA") :
			self.objMetaheuristic = SimulatedAnnealing(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
            
		if (self.metaheuristic == "DE") :
			self.objMetaheuristic = DifferentialEvolution(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
            
		if (self.metaheuristic == "HS") :
			self.objMetaheuristic = HarmonySearch(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
            
		if (self.metaheuristic == "CE") :
			self.objMetaheuristic = CrossEntropy(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
            
		if (self.metaheuristic == "CCE") :
			self.objMetaheuristic = CooperativeCrossEntropy(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
			            
		if (self.metaheuristic == "FWA") :
			self.objMetaheuristic = FireworksAlgorithm(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(SA.status.stateFinal) 
            
		if (self.metaheuristic == "CooS") :
			self.objMetaheuristic = CooperativeSearch(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(CooS.status.stateFinal)     
            
		if (self.metaheuristic == "RW") :
			self.objMetaheuristic = CooperativeSearch(self.problem, self.paraMetaheuristic, False) 
			# self.stats.add(CooS.status.stateFinal)     
							
		# self.problem.counter = Counter(self.nEvals)  
		
		# print("\n") 
		# self.stats.prints();
		# print("") 
		# self.stats.printAllSolutions();


	def run(self, sol = None):
		"""
		@return  :
		@author
		"""
     
		self.problem.counter = Counter(self.nEvals) 
		# self.stats.setLabel(self.metaheuristic +"---"+self.paraMetaheuristic+"["+str(self.nEvals)+"]");

		print("\n Experiments to "+self.metaheuristic) 
		self.objMetaheuristic.run(sol)
		self.stats.add(self.objMetaheuristic.status.stateFinal)   
				
		self.problem.counter = Counter(self.nEvals)  
		
		print("\n") 
# =============================================================================
# 		self.stats.prints();
# 		print("") 
# =============================================================================
		self.stats.printAllSolutions();
        
        
	def replacement(self, solution):
		"""
		@return  :
		@author
		""" 
     
		self.objMetaheuristic.replaceSolution(solution) 
        
        
	def getSolution(self, i = None):
		"""
		@return  :
		@author
		""" 
     
		if (i == None) :
			return self.stats.getSolutionComplete()
            
		else :
			return self.stats.getSolutionComplete(i)
