# SALogger
SALogger is a simple logging library for iOS tweaks.
It allows you to send your logs over UDP to your computer and view them in real time.

## Usage

1. Add `SALogger.dylib` and `SALogger.h` to your Theos project.  
2. Update your Makefile:

```
$(TWEAK_NAME)_LDFLAGS += -L$(THEOS_PROJECT_DIR)/path/to/SALogger -lSALogger
$(TWEAK_NAME)_CFLAGS += -I$(THEOS_PROJECT_DIR)/path/to/SALogger/include
```
3. Import and use in your tweak:
```
#import <SALogger.h>

%ctor {
    [SALogger setupWithHost:@"UR PC IP" port:5555];
    SALOG(@"Tweak loaded!");
}
```
4.Run python script and view logs
