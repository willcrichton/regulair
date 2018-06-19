NAME=regex_driver

DEVICE=1k
QUIET=-q
BUILD_DIR=build
PREFIX=$(BUILD_DIR)/$(NAME)

$(PREFIX).bin: $(PREFIX).v $(PREFIX).pcf
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(PREFIX).blif' $(PREFIX).v
	arachne-pnr $(QUIET) -d $(DEVICE) -o $(PREFIX).txt -p $(PREFIX).pcf $(PREFIX).blif
	icepack $(PREFIX).txt $(PREFIX).bin

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(PREFIX).v: $(NAME).py $(BUILD_DIR)
	magma -b icestick $(NAME).py

$(PREFIX).pcf: $(NAME).py $(BUILD_DIR)
	magma -b icestick $(NAME).py

upload: $(PREFIX).bin
	iceprog $(PREFIX).bin

upload_mac: $(PREFIX).bin
	iceprog $(PREFIX).bin

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all clean
