#include <3ds.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
    gfxInitDefault();
    consoleInit(GFX_BOTTOM, NULL);

    printf("FURRY SPIN 3DS!!\n");
    printf("\n");
    printf("Preparing the spin...\n");

    while (aptMainLoop())
    {
        hidScanInput();

        u32 kDown = hidKeysDown();

        if (kDown & KEY_START)
            break;

        gfxFlushBuffers();
        gfxSwapBuffers();
        gspWaitForVBlank();
    }

    gfxExit();
    return 0;
}
