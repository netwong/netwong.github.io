"use client";

import { useRef, useState, useEffect, type ChangeEvent, type MouseEvent } from "react";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Upload, ImageIcon } from "lucide-react";

interface PixelData {
  r: number;
  g: number;
  b: number;
}

interface MousePosition {
  x: number;
  y: number;
}

export default function ImageAnalyzer() {
  const { toast } = useToast();
  const [imageSrc, setImageSrc] = useState<string | null>(null);
  const [pixelData, setPixelData] = useState<PixelData | null>(null);
  const [mousePosition, setMousePosition] = useState<MousePosition | null>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const handleImageUpload = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (!file.type.startsWith('image/')) {
        toast({
          title: "Invalid File Type",
          description: "Please upload a valid image file (e.g., JPG, PNG).",
          variant: "destructive",
        });
        return;
      }
      const reader = new FileReader();
      reader.onload = (event) => {
        setImageSrc(event.target?.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const triggerFileUpload = () => {
    fileInputRef.current?.click();
  };

  useEffect(() => {
    if (imageSrc && canvasRef.current) {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext("2d", { willReadFrequently: true });
      if (ctx) {
        const img = new Image();
        img.src = imageSrc;
        img.onload = () => {
          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0);
          setPixelData(null);
          setMousePosition(null);
        };
        img.onerror = () => {
          toast({
            title: "Error",
            description: "Failed to load the image. The file might be corrupted or in an unsupported format.",
            variant: "destructive",
          });
          setImageSrc(null);
        }
      }
    }
  }, [imageSrc, toast]);

  const handleMouseMove = (e: MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    
    const canvasX = Math.floor((e.clientX - rect.left) * scaleX);
    const canvasY = Math.floor((e.clientY - rect.top) * scaleY);

    const ctx = canvas.getContext("2d");
    if (ctx && canvasX >= 0 && canvasX < canvas.width && canvasY >= 0 && canvasY < canvas.height) {
      const pixel = ctx.getImageData(canvasX, canvasY, 1, 1).data;
      setPixelData({ r: pixel[0], g: pixel[1], b: pixel[2] });
      setMousePosition({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY });
    } else {
      setPixelData(null);
      setMousePosition(null);
    }
  };

  const handleMouseLeave = () => {
    setPixelData(null);
    setMousePosition(null);
  };

  return (
    <Card className="w-full max-w-5xl shadow-lg border-2 border-primary/10 overflow-hidden">
        <div ref={containerRef} className="relative w-full aspect-video flex items-center justify-center p-2 bg-muted/20">
          {!imageSrc ? (
            <div className="flex flex-col items-center gap-4 text-center text-muted-foreground p-8">
                <ImageIcon className="w-16 h-16 text-primary/50" strokeWidth={1} />
              <h3 className="text-lg font-medium">Your image will appear here</h3>
              <p className="max-w-xs text-sm">Click the button below to upload an image. Most formats are supported.</p>
            </div>
          ) : (
            <canvas
              ref={canvasRef}
              onMouseMove={handleMouseMove}
              onMouseLeave={handleMouseLeave}
              className="max-w-full max-h-full object-contain cursor-crosshair rounded-md shadow-inner"
            />
          )}

          {mousePosition && pixelData && (
            <div
              className="absolute pointer-events-none z-10"
              style={{
                top: `${mousePosition.y}px`,
                left: `${mousePosition.x}px`,
                transform: 'translate(20px, 20px)',
              }}
            >
              <Card className="bg-background/80 backdrop-blur-sm shadow-xl animate-in fade-in zoom-in-95">
                <CardContent className="p-3">
                  <div className="flex items-center gap-3">
                    <div
                      className="w-8 h-8 rounded-md border"
                      style={{
                        backgroundColor: `rgb(${pixelData.r}, ${pixelData.g}, ${pixelData.b})`,
                      }}
                    />
                    <div className="font-mono text-sm space-y-0.5">
                      <div className="flex justify-between items-center gap-2"><span className="text-muted-foreground">R:</span> <span className="font-bold w-8 text-right text-foreground">{pixelData.r}</span></div>
                      <div className="flex justify-between items-center gap-2"><span className="text-muted-foreground">G:</span> <span className="font-bold w-8 text-right text-foreground">{pixelData.g}</span></div>
                      <div className="flex justify-between items-center gap-2"><span className="text-muted-foreground">B:</span> <span className="font-bold w-8 text-right text-foreground">{pixelData.b}</span></div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          )}
        </div>
        <div className="p-4 bg-background/50 rounded-b-lg border-t flex justify-center">
            <input
                type="file"
                ref={fileInputRef}
                onChange={handleImageUpload}
                accept="image/png, image/jpeg, image/gif, image/webp"
                className="hidden"
            />
            
            <Button onClick={triggerFileUpload} variant="default" className="bg-accent text-accent-foreground hover:bg-accent/90 focus-visible:ring-accent">
                <Upload className="mr-2 h-4 w-4" />
                {imageSrc ? "Upload Another Image" : "Upload Image"}
            </Button>
        </div>
    </Card>
  );
}
