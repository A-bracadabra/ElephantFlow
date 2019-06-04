
action _nop() { }
/********** data_valid_tbl **********/
action ipv4_valid_act() {
	modify_field(md.data_valid, 1);
	add_to_field(ipv4.ttl, -1);
}
table data_valid_tbl {
	reads {
		ipv4 : valid;
	}
	actions {
		_nop;
		ipv4_valid_act;
	}
}

/********** ipv4_route_tbl **********/
action ipv4_route_act(egress_port) {
	modify_field(ig_intr_md_for_tm.ucast_egress_port, egress_port);
}
action ipv4_default_route(default_port) {
	modify_field(ig_intr_md_for_tm.ucast_egress_port, default_port);
}
table ipv4_route_tbl {
	reads {
		ipv4.dstAddr : ternary;
	}
	actions {
		ipv4_route_act;
		ipv4_default_route;
	}

}
/********** key_route_tbl **********/
action key_route_act(key_port) {
	modify_field(ig_intr_md_for_tm.ucast_egress_port, key_port);
}
table key_route_tbl {
	reads {
		md.bf1 : exact;
		md.bf2 : exact;
	}
	actions {
		key_route_act;
		_nop;
	}
}

/********** add_header_tbl **********/
action add_header_act() {
	add_header(ad);
}
table add_header_tbl {
	reads {
		ig_intr_md_for_tm.ucast_egress_port : exact;
	}
	actions {
		add_header_act;
		_nop;
	}
}

/********** set_index_tbl **********/

field_list_calculation hash_11 {
    input {
        hash_1_field_list;
    }
    algorithm : crc_16;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_12 {
    input {
        hash_1_field_list;
    }
    algorithm : crc_16_buypass;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_13 {
    input {
        hash_1_field_list;
    }
    algorithm : crc_16_dds_110;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_14 {
    input {
        hash_1_field_list;
    }
    algorithm : crc_16_dect;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_21 {
    input {
        hash_2_field_list;
    }
    algorithm : crc_16;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_22 {
    input {
        hash_2_field_list;
    }
    algorithm : crc_16_buypass;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_23 {
    input {
        hash_2_field_list;
    }
    algorithm : crc_16_dds_110;
    output_width : COUNT_MIN_HASH_WIDTH;
}
field_list_calculation hash_24 {
    input {
        hash_2_field_list;
    }
    algorithm : crc_16_dect;
    output_width : COUNT_MIN_HASH_WIDTH;
}
action set_index11_act() {
	modify_field_with_hash_based_offset(md.index11, 0, hash_11, REG_MAX_LEN);
}
action set_index12_act() {
	modify_field_with_hash_based_offset(md.index12, 0, hash_12, REG_MAX_LEN);
}
action set_index13_act() {
	modify_field_with_hash_based_offset(md.index13, 0, hash_13, REG_MAX_LEN);
}
action set_index14_act() {
	modify_field_with_hash_based_offset(md.index14, 0, hash_14, REG_MAX_LEN);
}
action set_index21_act() {
	modify_field_with_hash_based_offset(md.index21, 0, hash_21, REG_MAX_LEN);
}
action set_index22_act() {
	modify_field_with_hash_based_offset(md.index22, 0, hash_22, REG_MAX_LEN);
}
action set_index23_act() {
	modify_field_with_hash_based_offset(md.index23, 0, hash_23, REG_MAX_LEN);
}
action set_index24_act() {
	modify_field_with_hash_based_offset(md.index24, 0, hash_24, REG_MAX_LEN);
}
table set_index11_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index11_act;
	}
}
table set_index12_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index12_act;
	}
}
table set_index13_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index13_act;
	}
}
table set_index14_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index14_act;
	}
}
table set_index21_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index21_act;
	}
}
table set_index22_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index22_act;
	}
}
table set_index23_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index23_act;
	}
}
table set_index24_tbl {
	reads {
		md.temp : exact;
	}
	actions {
		set_index24_act;
	}
}
control set_index {
	apply(set_index11_tbl);
	apply(set_index12_tbl);
	apply(set_index13_tbl);
	apply(set_index14_tbl);
	apply(set_index21_tbl);
	apply(set_index22_tbl);
	apply(set_index23_tbl);
	apply(set_index24_tbl);
}
/********** set_index1/2 ***********/
action set_index1_act() {
	modify_field(ad.index11, md.index11);
	modify_field(ad.index12, md.index12);
	modify_field(ad.index13, md.index13);
	modify_field(ad.index14, md.index14);
}
table set_index1_tbl {
	actions {
		set_index1_act;
	}
}

action set_index2_act() {
	modify_field(ad.index21, md.index21);
	modify_field(ad.index22, md.index22);
	modify_field(ad.index23, md.index23);
	modify_field(ad.index24, md.index24);
}
table set_index2_tbl {
	actions {
		set_index2_act;
	}
}




register temp {
	width: 1;
	instance_count: 1;
}
blackbox stateful_alu stateful_temp {
	reg: temp;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.temp;
}
action temp_act (){
	stateful_temp.execute_stateful_alu(0);
}
table temp_tbl {
	actions {
		temp_act;
	}
}
action temp_route_act(key_port) {
	modify_field(ig_intr_md_for_tm.ucast_egress_port, key_port);
}
table temp_route_tbl {
	actions {
		temp_route_act;
	}
}