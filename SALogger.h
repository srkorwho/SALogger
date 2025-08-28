#import <Foundation/Foundation.h>

#define SALOG(fmt, ...) [SALogger log:[NSString stringWithFormat:(fmt), ##__VA_ARGS__]]

@interface SALogger : NSObject
+ (void)setupWithHost:(NSString *)host port:(int)port;
+ (void)log:(NSString *)message;
@end
