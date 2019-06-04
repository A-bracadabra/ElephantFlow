import pd_base_tests

from ptf import config
from ptf.testutils import *
from ptf.thriftutils import *

from elephant-flow.p4_pd_rpc.ttypes import *
from res_pd_rpc.ttypes import *


import time
import os
import threading

# ingress_port = 128
# egress_port  = 128
default_port = 128
key_port = 129
mac_da       = "00:11:11:11:11:11"
ip_dst='10.0.0.1'



datas = []
ipv4s = []
count = 0

class Data(object):
	def __init__(self, ipv4, index1, index2, index3, index4, count = 0):
		self.ipv4 = ipv4

		self.index1 = index1
		self.index2 = index2
		self.index3 = index3
		self.index4 = index4

		self.count = count

	def setCount(self, count):
		self.count = count

	def allPrint(self):
		print ("ipv4            :	"), i32_to_ipv4Addr(self.ipv4)
		print ("hit number      :	"), self.count
		print

	def getIndex(self):
		return [self.index1, self.index2, self.index3, self.index4]

class test(pd_base_tests.ThriftInterfaceDataPlane):
    def __init__(self):
        pd_base_tests.ThriftInterfaceDataPlane.__init__(self,
                                                        ["elephant-flow"])


    def getPort(self, port_id, chann_id):
        if True:
            return port_id
        else:
            return port_id
 
    def enablePort(self, port_id, chann_id, speed):
        self.pltfm_pm.pltfm_pm_port_add(self.dev, self.getPort(port_id, chann_id), speed, 0)
        self.pltfm_pm.pltfm_pm_port_an_set(self.dev, self.getPort(port_id, chann_id), 2)
        self.pltfm_pm.pltfm_pm_port_enable(self.dev, self.getPort(port_id, chann_id))
 
    def setUpPorts(self):
        speed_10g=2
        #port_id=[128,129,130,131,160,161,162,163,168,169,170,171,28,29,30,31,20,21,22,23]
        port_id=[66,67]
        for port in port_id:
            self.enablePort(port, 0, speed_10g)



    def setUp(self):
        pd_base_tests.ThriftInterfaceDataPlane.setUp(self)

        self.sess_hdl = self.conn_mgr.client_init()
        self.dev      = 0
        self.dev_tgt  = DevTarget_t(self.dev, hex_to_i16(0xFFFF))

	
        print("\nConnected to Device %d, Session %d" % (
            self.dev, self.sess_hdl))
        # self.setUpPorts()
    
    def setTimer(self):
        global timer
        timer = threading.Timer(100,self.setTimer)
        timer.start()
        # self.setCount(datas)
        self.fileWrite()
        # self.rewriteReg()
        self.resetReg()
        
        print "---Timer---"
        # if datas:
        #     print "- * - * - * - * - * - * - * - * - * - * -"
        #     for data in datas:
        #         data.allPrint()
        #     del datas[:]
        #     del ipv4s[:]
        #     print
        #     print

    def setTable(self):


        def data_valid_table():
            self.client.data_valid_tbl_set_default_action__nop(
                self.sess_hdl, self.dev_tgt)

            self.client.data_valid_tbl_table_add_with_ipv4_valid_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))


        def ipv4_route_table():
            self.client.ipv4_route_tbl_set_default_action_ipv4_default_route(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_ipv4_default_route_action_spec_t(
                    action_default_port = default_port))

        def key_route_table():
            self.client.key_route_tbl_set_default_action_key_route_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_key_route_act_action_spec_t(
                    action_key_port = key_port))

            self.client.key_route_tbl_table_add_with__nop(
                self.sess_hdl, self.dev_tgt, 
                elephant-flow_key_route_tbl_match_spec_t(1, 1))


        def set_count_min1_table():
            self.client.count_min1_table_1_set_default_action_count_min1_act_1(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.count_min1_table_2_set_default_action_count_min1_act_2(
                self.sess_hdl, self.dev_tgt) 

            self.client.count_min1_table_3_set_default_action_count_min1_act_3(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.count_min1_table_4_set_default_action_count_min1_act_4(
                self.sess_hdl, self.dev_tgt) 
        def set_count_min2_table():
            self.client.count_min2_table_1_set_default_action_count_min2_act_1(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.count_min2_table_2_set_default_action_count_min2_act_2(
                self.sess_hdl, self.dev_tgt) 

            self.client.count_min2_table_3_set_default_action_count_min2_act_3(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.count_min2_table_4_set_default_action_count_min2_act_4(
                self.sess_hdl, self.dev_tgt) 


        def set_bf1_table():
            self.client.bf1_table_1_set_default_action_bf1_act_1(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.bf1_table_2_set_default_action_bf1_act_2(
                self.sess_hdl, self.dev_tgt) 

            self.client.bf1_table_3_set_default_action_bf1_act_3(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.bf1_table_4_set_default_action_bf1_act_4(
                self.sess_hdl, self.dev_tgt) 
        def set_bf2_table():
            self.client.bf2_table_1_set_default_action_bf2_act_1(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.bf2_table_2_set_default_action_bf2_act_2(
                self.sess_hdl, self.dev_tgt) 

            self.client.bf2_table_3_set_default_action_bf2_act_3(
                self.sess_hdl, self.dev_tgt)    
    
            self.client.bf2_table_4_set_default_action_bf2_act_4(
                self.sess_hdl, self.dev_tgt) 

        def add_header_table():
            self.client.add_header_tbl_set_default_action__nop(
                self.sess_hdl, self.dev_tgt)

            self.client.add_header_tbl_table_add_with_add_header_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_add_header_tbl_match_spec_t(key_port))


        def set_index_table():
            self.client.set_index11_tbl_table_add_with_set_index11_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index12_tbl_table_add_with_set_index12_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index13_tbl_table_add_with_set_index13_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index14_tbl_table_add_with_set_index14_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))   

            self.client.set_index21_tbl_table_add_with_set_index21_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index22_tbl_table_add_with_set_index22_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index23_tbl_table_add_with_set_index23_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))

            self.client.set_index24_tbl_table_add_with_set_index24_act(
                self.sess_hdl, self.dev_tgt,
                elephant-flow_data_valid_tbl_match_spec_t(1))


            self.client.set_index1_tbl_set_default_action_set_index1_act(
                self.sess_hdl, self.dev_tgt)
            self.client.set_index2_tbl_set_default_action_set_index2_act(
                self.sess_hdl, self.dev_tgt)
        
        data_valid_table()
        ipv4_route_table()
        key_route_table()
        add_header_table()
        set_index_table()

        set_count_min1_table()
        set_count_min2_table()
        set_bf1_table()
        set_bf2_table()

        

    def setCount(self, datas):
    	if not datas:
    		return
    	for data in datas:
            count1 = self.client.register_read_count_min1_reg_1(self.sess_hdl, self.dev_tgt, data.getIndex()[0], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count2 = self.client.register_read_count_min1_reg_2(self.sess_hdl, self.dev_tgt, data.getIndex()[1], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count3 = self.client.register_read_count_min1_reg_3(self.sess_hdl, self.dev_tgt, data.getIndex()[2], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count4 = self.client.register_read_count_min1_reg_4(self.sess_hdl, self.dev_tgt, data.getIndex()[3], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            min_count = count1
            if min_count > count2:
                min_count = count2
            if min_count > count3:
                min_count = count3
            if min_count > count4:
                min_count = count4
            count = min_count

            count1 = self.client.register_read_count_min2_reg_1(self.sess_hdl, self.dev_tgt, data.getIndex()[0], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count2 = self.client.register_read_count_min2_reg_2(self.sess_hdl, self.dev_tgt, data.getIndex()[1], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count3 = self.client.register_read_count_min2_reg_3(self.sess_hdl, self.dev_tgt, data.getIndex()[2], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            count4 = self.client.register_read_count_min2_reg_4(self.sess_hdl, self.dev_tgt, data.getIndex()[3], flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]
            min_count = count1
            if min_count > count2:
                min_count = count2
            if min_count > count3:
                min_count = count3
            if min_count > count4:
                min_count = count4
            count += min_count
            data.setCount(count)
        return

    def scoreData(self, pkt):
    	if not pkt:
    		return
    	s = pkt
    	ipv4_srcAddr = (ord(s[60]) << 24) + (ord(s[61]) << 16) + (ord(s[62]) << 8) + ord(s[63])
    	ipv4_dstAddr = (ord(s[64]) << 24) + (ord(s[65]) << 16) + (ord(s[66]) << 8) + ord(s[67])
    	

    	index1 = (ord(s[16]) << 24) + (ord(s[17]) << 16) + (ord(s[18]) << 8) + ord(s[19])
    	index2 = (ord(s[20]) << 24) + (ord(s[21]) << 16) + (ord(s[22]) << 8) + ord(s[23])
    	index3 = (ord(s[24]) << 24) + (ord(s[25]) << 16) + (ord(s[26]) << 8) + ord(s[27])
    	index4 = (ord(s[28]) << 24) + (ord(s[29]) << 16) + (ord(s[30]) << 8) + ord(s[31])
        if index1 :
            pkt_data = Data(ipv4_srcAddr, index1, index2, index3, index4)
            if ipv4_srcAddr not in ipv4s:
                ipv4s.append(ipv4_srcAddr)
                datas.append(pkt_data)

        index1 = (ord(s[32]) << 24) + (ord(s[33]) << 16) + (ord(s[34]) << 8) + ord(s[35])
        index2 = (ord(s[36]) << 24) + (ord(s[37]) << 16) + (ord(s[38]) << 8) + ord(s[39])
        index3 = (ord(s[40]) << 24) + (ord(s[41]) << 16) + (ord(s[42]) << 8) + ord(s[43])
        index4 = (ord(s[44]) << 24) + (ord(s[45]) << 16) + (ord(s[46]) << 8) + ord(s[47])

        if index1 :
            pkt_data = Data(ipv4_dstAddr, index1, index2, index3, index4)
            if ipv4_dstAddr not in ipv4s:
                ipv4s.append(ipv4_dstAddr)
                datas.append(pkt_data)
    	

    def fileWrite(self):
        global count
        filename = "datas/" + str(count) + ".txt"
        with open(filename, 'w') as f:
            for i in range(512):
                f.write(str(self.client.register_read_count_min1_reg_1(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min1_reg_2(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min1_reg_3(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min1_reg_4(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min2_reg_1(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min2_reg_2(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min2_reg_3(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
            for i in range(512):
                f.write(str(self.client.register_read_count_min2_reg_4(self.sess_hdl, self.dev_tgt, i, flags=elephant-flow_register_flags_t(read_hw_sync = True))[0]))
                f.write(" ")
            f.write("\n")
        f.close()
        count += 1


    def resetReg(self):
        self.client.register_reset_all_temp(self.sess_hdl, self.dev_tgt)

        self.client.register_reset_all_bf1_reg_1(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf1_reg_2(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf1_reg_3(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf1_reg_4(self.sess_hdl, self.dev_tgt)

        self.client.register_reset_all_bf2_reg_1(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf2_reg_2(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf2_reg_3(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_bf2_reg_4(self.sess_hdl, self.dev_tgt)

        self.client.register_reset_all_count_min1_reg_1(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min1_reg_2(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min1_reg_3(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min1_reg_4(self.sess_hdl, self.dev_tgt)

        self.client.register_reset_all_count_min2_reg_1(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min2_reg_2(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min2_reg_3(self.sess_hdl, self.dev_tgt)
        self.client.register_reset_all_count_min2_reg_4(self.sess_hdl, self.dev_tgt)

    def rewriteReg(self):

        self.client.register_write_all_count_min2_reg_1(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min2_reg_2(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min2_reg_3(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min2_reg_4(
			self.sess_hdl, self.dev_tgt, 0)

        self.client.register_write_all_count_min1_reg_1(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min1_reg_2(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min1_reg_3(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_count_min1_reg_4(
            self.sess_hdl, self.dev_tgt, 0)

        self.client.register_write_all_bf1_reg_1(
			self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf1_reg_2(
			self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf1_reg_3(
			self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf1_reg_4(
			self.sess_hdl, self.dev_tgt, 0)

        self.client.register_write_all_bf2_reg_1(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf2_reg_2(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf2_reg_3(
            self.sess_hdl, self.dev_tgt, 0)
        self.client.register_write_all_bf2_reg_4(
            self.sess_hdl, self.dev_tgt, 0)
 

    def runTest(self):

        print("Populating table entries")
        # self.setTable()
        self.setTimer()

	


        self.conn_mgr.complete_operations(self.sess_hdl)
  

        #self.setUpPorts()


        # pkt = simple_tcp_packet(eth_dst=mac_da,
        #                         eth_src='00:55:55:55:55:55',
        #                         ip_dst='11.0.0.1',
        #                         ip_id=101,
        #                         ip_ttl=128,
        #                         ip_ihl=5)


        # while True:
        #     send_packet(self, ingress_port, pkt)
        #     (rcv_device, rcv_port, pkt_ex, pkt_time) = dp_poll(self, 0, key_port)
        #     if rcv_port: 
        #         self.scoreData(pkt_ex)
        while True:
            pass




    def tearDown(self):
        try:
            print("Clearing table entries")
            for table in self.entries.keys():
                delete_func = "self.client." + table + "_table_delete"
                for entry in self.entries[table]:
                    exec delete_func + "(self.sess_hdl, self.dev, entry)"
        except:
            print("Error while cleaning up. ")
            print("You might need to restart the driver")
        finally:
            self.conn_mgr.complete_operations(self.sess_hdl)
            self.conn_mgr.client_cleanup(self.sess_hdl)
            print("Closed Session %d" % self.sess_hdl)
            pd_base_tests.ThriftInterfaceDataPlane.tearDown(self)
