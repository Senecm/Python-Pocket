# Quantum [qiskit] Notes

## Basic setup
To use qiskit, one must have the module and an API key. Once obtained, the following code will save that key to the machine:
### Checking the version
```
import qiskit
qiskit.__qiskit_version__ #displays version
```
## Saving API token
```
from qiskit import IBMQ
IBMQ.save_account('token') #saves account to machine
IBMQ.load_account()
```
## Basic entanglement
```
from qiskit import *
qr = QuantumRegister(2) #specifies the number of qbits
cr = ClassicalRegister(2) #specifies the number of bits
circuit = QuantumCircuit(qr, cr) #initialises the circuit
matplotlib inline #prepare drawing tools >side note, comments cant be on this line!
circuit.draw() #draw circut
circuit.h(qr[0]) #applying a hadamard gate (quantum logic gate)
circuit.draw(output="mpl") #visualising the circuit 
```
## Measurment of qbits
```
circuit.measure(qr, cr) #measuring the qbits, forcing them to exit superposition, and storing them in normal bits
```
## Simulating circuits
```
simulator = Aer.get_backend("qasm_simulator") #contacting the simulator, 'quantum assembly lanuage'
exc = execute(circuit, backend=simulator).result() #executing the circuit, with qasm_simulator,
res = exc.results() #relays results
```
## Displaying results
```
from qiskit.tools.visualization import plot_histogram #importing historgram visulisation
plot_histogram(res.get_counts(circuit)) #dispaling the circuit
```
## Using a quantum computer
```
IBMQ.load_account() #loading account
provider = IBMQ.get_provider("ibm-q") #getting the list of avaliable machines
qcomp = provider.get_backend("ibmq_16_melbourne") #getting the quantum computer
job = execute(circuit, backend=qcomp)
job_monitor(job) #queing the job, running when avaliable
result = job.result() #relaying results
plot_histogram(result.get_counts(circuit)) #visualising results
```
>note, the difference in simulations are a result of the simluator being a perfect quantum machine, and the actual quantum machine contianing small quantum errors which are being rectifyed daily