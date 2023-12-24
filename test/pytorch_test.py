import torch


def test_backward_propagation():
    x1 = torch.Tensor([2.0]).double()
    x2 = torch.Tensor([0.0]).double()
    w1 = torch.Tensor([-3.0]).double()
    w2 = torch.Tensor([1.0]).double()
    b = torch.tensor([6.8813735870195432]).double()

    x1.requires_grad = True
    x2.requires_grad = True
    w1.requires_grad = True
    w2.requires_grad = True
    b.requires_grad = True

    n = x1 * w1 + x2 * w2 + b
    o = torch.tanh(n)

    o.backward()

    assert round(x1.grad.item(), 1) == -1.5
    assert round(x2.grad.item(), 1) == 0.5
    assert round(w1.grad.item(), 1) == 1.0
    assert round(w2.grad.item(), 1) == 0.0
