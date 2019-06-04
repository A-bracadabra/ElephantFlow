header_type metadata_hdr {
	fields {
		data_valid: 1;	//判断数据包是否合法，主要看路由是否准确，准确则置1
		temp : 1;

		bf1: 1;	
		bf1_1: 1;
		bf1_2: 1;
		bf1_3: 1;
		bf1_4: 1;

		bf2: 1;	
		bf2_1: 1;
		bf2_2: 1;
		bf2_3: 1;
		bf2_4: 1;

		cm1: 1;
		cm1_1: 1;
		cm1_2: 1;
		cm1_3: 1;
		cm1_4: 1;
	
		cm2: 1;
		cm2_1: 1;
		cm2_2: 1;
		cm2_3: 1;
		cm2_4: 1;

		index11 : 16;
        index12 : 16;
        index13 : 16;
        index14 : 16;
        index21 : 16;
        index22 : 16;
        index23 : 16;
        index24 : 16;
	}
}

header_type metadata_hash_1_hdr {
	fields {
		srcAddr: 32;
	}
}
header_type metadata_hash_2_hdr {
	fields {
		dstAddr: 32;
	}
}

metadata metadata_hdr md;
metadata metadata_hash_1_hdr md_hash_1;
metadata metadata_hash_2_hdr md_hash_2;

field_list hash_1_field_list {
	md_hash_1;
}
field_list hash_2_field_list {
	md_hash_2;
}