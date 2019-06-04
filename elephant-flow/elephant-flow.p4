#include <tofino/intrinsic_metadata.p4>
#include <tofino/constants.p4>
#include <tofino/primitives.p4>
#include "tofino/stateful_alu_blackbox.p4"


#include "includes/header.p4"
#include "includes/tofino.p4"
#include "includes/defines.p4"
#include "includes/parser.p4"


#include "count_min1.p4"
#include "bloom_filter1.p4"
#include "count_min2.p4"
#include "bloom_filter2.p4"
#include "valid.p4"

control ingress {
	apply(data_valid_tbl);
	if (md.data_valid == 1) {
		apply(ipv4_route_tbl);
		set_index();
		count_min1();
		count_min2();
		if (md.cm1 == 1 or md.cm2 == 1) {
			if (md.cm1 == 1) {bf1();}
			if (md.cm2 == 1) {bf2();}
			if ((md.cm1 == 1 and md.bf1 == 0) or (md.cm2 == 1 and md.bf2 == 0)) {
				apply(key_route_tbl);
				
			}
		}
	}
	apply(temp_tbl);

}
control egress {
	apply(add_header_tbl);
	if (md.temp == 0) {
		apply(temp_route_tbl);
	}
	else {
	    if (md.cm1 == 1 and md.bf1 == 0) {apply(set_index1_tbl);}
    	if (md.cm2 == 1 and md.bf2 == 0) {apply(set_index2_tbl);}
    }
}