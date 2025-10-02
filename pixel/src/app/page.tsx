import ImageAnalyzer from "@/components/image-analyzer";

export default function Home() {
  return (
    <main className="flex min-h-screen w-full flex-col items-center justify-center bg-background p-4 sm:p-8 md:p-12">
      <div className="w-full max-w-7xl mx-auto flex flex-col items-center">
        <header className="text-center mb-8">
          <h1 className="text-4xl md:text-5xl font-headline font-bold text-foreground">
            Pixel Probe
          </h1>
          <p className="mt-2 text-lg text-muted-foreground">
            Upload an image and hover to inspect pixel-perfect color data.
          </p>
        </header>
        <ImageAnalyzer />
      </div>
    </main>
  );
}
