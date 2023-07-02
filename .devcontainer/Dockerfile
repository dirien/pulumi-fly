FROM  --platform=linux/amd64 pulumi/pulumi:3.74.0

# Install pulumictl and set to PATH
RUN curl -fsSL https://get.pulumi.com | sh
ENV PATH="/root/.pulumi/bin:${PATH}"

# create a directory for pulumictl and download the binary to it and set to PATH
RUN mkdir -p /root/pulumictl && cd /root/pulumictl/
RUN wget https://github.com/pulumi/pulumictl/releases/download/v0.0.42/pulumictl-v0.0.42-linux-amd64.tar.gz -O /root/pulumictl/pulumictl-v0.0.42-linux-amd64.tar.gz
RUN tar -xvf /root/pulumictl/pulumictl-v0.0.42-linux-amd64.tar.gz -C /root/pulumictl/
ENV PATH="//root/pulumictl/:${PATH}"
