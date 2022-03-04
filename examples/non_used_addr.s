.data                   ; start of data section
    X:      .word   3
            .word   0
            .word   0
    Y:      .word   2
    Z:      .word   0
    VRAM:   .addr   0x8000
.text                   ; start of text section
    main:               ; main function
        LDA X           ; o acumulador recebe o valor de X
        ADD Y           ; o acumulador é somado com Y
        STA Z           ; o acumulador é copiado para Z
        LDI 0xFF         ; o acumulador recebe o valor 1
        HLT             ; o processador para
