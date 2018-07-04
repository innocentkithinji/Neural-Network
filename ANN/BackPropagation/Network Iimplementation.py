from NetworkClass import Network
from neuronClass import Neuron

if __name__ == '__main__':
    topology = [2, 3, 2]
    net = Network(topology)
    Neuron.eta = 0.09
    Neuron.alpha = 0.015
    while True:

        err = 0
        inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
        outputs = [[0, 0], [1, 0], [1, 0], [0, 1]]
        for i in range(len(inputs)):
            net.setInput(inputs[i])
            net.feedForword()
            net.backPropagate(outputs[i])
            err = err + net.getError(outputs[i])
        print("error: ", err)
        if err < 0.02:
            break

    while True:
        a = int(input("type 1st input :"))
        b = int(input("type 2nd input :"))

        net.setInput([a, b])
        net.feedForword()
        print(net.getThResults())
