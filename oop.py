# class HumanServey:
#     def __init__(self, name, age, marital_status, kids):
#         self.name = name
#         self.age = age
#         self.marital_status = marital_status
#         self.kids = kids

#     def introduce(self):
#         return f"Hey, I am {self.name}. I am {self.age} years old. I am {self.marital_status}. I have {len(self.kids)} kids"

# moinul_instance = HumanServey("Md. Moinul Islam", 26, "Unmarried", [])
# gaziul_instance = HumanServey("Md. Gaziul Islam", 60, "Married", ["Shoron", "Mobin", "Shorna"])

# print(moinul_instance.introduce())
# print(gaziul_instance.introduce())


class EC2Server:
    def __init__(self, server_id, ip_address, instance_type, status="stopped"):
        self.server_id = server_id
        self.ip_address = ip_address
        self.instance_type = instance_type
        self.status = status

    def serverStatus(self):
        if self.status == "starting":
            return f"Server id : {self.server_id}, Server ip address : {self.ip_address}, Server instance : {self.instance_type} and server is running"
        else:
            return f"Server id : {self.server_id}, Server ip address : {self.ip_address}, Server instance : {self.instance_type} and server is stopped"

web_server = EC2Server("i-099x123", "54.210.2.1", "t3.medium", "starting")
db_server = EC2Server("i-088x456", "10.0.1.4", "r5.large")
app_server = EC2Server("i-077x789", "172.16.1.10", "t3.large", "starting")
dev_server = EC2Server("i-066x321", "192.168.1.10", "t2.micro", "stopped")
test_server = EC2Server("i-055x654", "10.0.2.5", "t3.small", "starting")
backup_server = EC2Server("i-044x987", "172.16.2.20", "m5.large")

print(web_server.serverStatus())
print(db_server.serverStatus())
print(app_server.serverStatus())
print(dev_server.serverStatus())
print(test_server.serverStatus())
print(backup_server.serverStatus())
