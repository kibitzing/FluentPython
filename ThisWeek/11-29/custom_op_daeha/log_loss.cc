#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/shape_inference.h"
#include "tensorflow/core/framework/op_kernel.h"

using namespace tensorflow;

REGISTER_OP("LogLoss")
    .Input("real: float32")
    .Input("pred: float32")
    .Output("loss: float32");


class LogLossOp : public OpKernel {
 public:
  explicit LogLossOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {

    // Grab the prediction tensor
    const Tensor& pred_tensor = context->input(1);
    auto pred = pred_tensor.flat<float>();

    // Grab the y tensor
    const Tensor& y_tensor = context->input(0);
    auto y = y_tensor.flat<float>();

    // Create an output tensor
    // Allocates a scalar decimal value
    
    Tensor* output_tensor = nullptr;
    OP_REQUIRES_OK(context,
                   context->allocate_output(0, TensorShape(), &output_tensor));
    auto loss = output_tensor->template scalar<float>();

    int N = pred.size();

    // Avoid log(0)
    float epsilon = 1e-7;

    for ( int i=0; i<N; i++ ) {
      loss() = loss() + -( (y(i) * log(pred(i) + epsilon)) + (1 - y(i)) * log(1 - pred(i) + epsilon) );
    }
  }
};

REGISTER_KERNEL_BUILDER(Name("LogLoss").Device(DEVICE_CPU), LogLossOp);
