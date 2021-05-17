while read -r line;
do
        echo $line | rabbitmqadmin publish exchange=amq.default routing_key=hello ;
done < m #Where m is a file containing your messages
