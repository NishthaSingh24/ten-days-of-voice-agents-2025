import * as React from 'react';
import { type VariantProps, cva } from 'class-variance-authority';
import { Slot } from '@radix-ui/react-slot';
import { cn } from '@/lib/utils';

const buttonVariants = cva(
  [
    'text-xs font-bold tracking-wider uppercase whitespace-nowrap',
    'inline-flex items-center justify-center gap-2 shrink-0 rounded-full cursor-pointer outline-none transition-all duration-300',
    'focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]',
    'disabled:pointer-events-none disabled:opacity-50',
    'aria-invalid:ring-destructive/20 aria-invalid:border-destructive dark:aria-invalid:ring-destructive/40 ',
    "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0",
  ],
  {
    variants: {
      variant: {
        default:
          'bg-muted text-foreground hover:bg-muted focus:bg-muted hover:bg-foreground/10 hover:shadow-md',
        destructive: [
          'bg-destructive/10 text-destructive',
          'hover:bg-destructive/20 focus:bg-destructive/20 focus-visible:ring-destructive/20 hover:shadow-md',
          'dark:focus-visible:ring-destructive/40',
        ],
        outline: [
          'border-2 border-input bg-background',
          'hover:bg-accent hover:text-accent-foreground hover:border-primary hover:shadow-md',
          'dark:bg-input/30 dark:border-input dark:hover:bg-input/50',
        ],
        primary:
          'bg-gradient-to-r from-primary to-accent text-primary-foreground hover:from-primary/90 hover:to-accent/90 focus:from-primary/90 focus:to-accent/90 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5',
        secondary:
          'bg-foreground/15 text-secondary-foreground hover:bg-foreground/20 hover:shadow-md',
        ghost:
          'hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50 hover:shadow-sm',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-9 px-4 py-2 has-[>svg]:px-3',
        sm: 'h-8 gap-1.5 px-3 has-[>svg]:px-2.5',
        lg: 'h-12 px-8 has-[>svg]:px-6 text-sm',
        icon: 'size-9',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<'button'> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean;
  }) {
  const Comp = asChild ? Slot : 'button';

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  );
}

export { Button, buttonVariants };
