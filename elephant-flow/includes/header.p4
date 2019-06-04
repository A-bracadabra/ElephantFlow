
header_type ethernet_hdr {
	fields {
		dst : 48;
		src : 48;
		ethtype : 16;
	}
}
header_type ipv4_hdr {
	fields {
		version : 4;
		ihl : 4;
		diffserv : 8;
		totalLen : 16;
		identification : 16;
		flags : 3;
		fragOffset : 13;
		ttl : 8;
		protocol : 8;
		checksum : 16;
		srcAddr : 32;
		dstAddr : 32;
	}
}
header_type add_hdr {
    fields {
        ethtype : 16;
        index11 : 32;
        index12 : 32;
        index13 : 32;
        index14 : 32;
        index21 : 32;
        index22 : 32;
        index23 : 32;
        index24 : 32;
    }
}

header ethernet_hdr eth;
header ipv4_hdr ipv4;
header add_hdr ad;