using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace resizesearchmap
{
    class Program
    {
        // A cache of all opacity values (0-255) scaled down to 0-1 for performance
        private static readonly float[] _opacities = Enumerable.Range(0, 256)
                                              .Select(o => o / 255f)
                                              .ToArray();

        private static Color AlphaComposite(Color c1, Color c2, byte A2)
        {
            var opa1 = _opacities[c1.A];
            var opa2 = _opacities[A2];
            var ar = opa1 + opa2 - (opa1 * opa2);
            var asr = opa2 / ar;
            var a1 = 1 - asr;
            var a2 = asr * (1 - opa1);
            var ab = asr * opa1;
            var r = (byte)(c1.R * a1 + c2.R * a2 + c2.R * ab);
            var g = (byte)(c1.G * a1 + c2.G * a2 + c2.G * ab);
            var b = (byte)(c1.B * a1 + c2.B * a2 + c2.B * ab);
            return Color.FromArgb((byte)(ar * 255), r, g, b);
        }

        static bool ce(Color c1, Color c2)
        {
            return (c1.R == c2.R && c1.G == c2.G && c1.B == c2.B);
        }

        static bool cek(Color c1, Color[] ca)
        {
            foreach (var c in ca)
                if (ce(c1, c))
                    return true;
            return false;
        }

        static void ProcessFile(string origFilePath, bool sr2)
        {
            Console.WriteLine(Path.GetFileName(origFilePath));

            string searchFileName = origFilePath.Replace(".bmp", "SR.bmp");
            string outFileName = origFilePath.Replace(".bmp", "SR_res.bmp");
            if (sr2)
                outFileName = origFilePath.Replace(".bmp", "SR_res2.bmp");

            if (!File.Exists(searchFileName))
            {
                Console.WriteLine($"{Path.GetFileName(searchFileName)} does not exist!");
                return;
            }

            if (File.Exists(outFileName))
            {
                Console.WriteLine($"{Path.GetFileName(outFileName)} already exist!");
                return;
            }

            Color iObstacle = Color.Black; // ReservedBlocked | 0 - Obstacle - impassable, light blocking (black)
            Color iSand = Color.Maroon; // Dirt | 1 - Sand ? (burgandy)
            Color iWood1 = Color.Green; // Wood | 2 - Wood (green)
            Color iWood2 = Color.Brown; // Wood | 3 - Wood (brown)
            Color iStoneEcho = Color.Navy; // Metal ? Stone | 4 - Stone - echo-ey (dark blue)
            Color iGrass = Color.Purple; // Grass | 5 - Grass - soft (purple)
            Color iWater = Color.Teal; // Water | 6 - Water - passable (turquoise)
            Color iStoneHard = Color.Silver; // Stone | 7 - Stone - hard (light gray)
            Color iFlyover = Color.Gray; // ReservedFlyOver | 8 - Obstacle - impassable, non light blocking (dark grey)
            Color iWood = Color.Red; // Wood | 9 - Wood (red)
            Color iWall = Color.LightGreen; // ReservedBlocked | 10 - Wall - impassable (bright green) ! not found
            Color iSnow = Color.Yellow; // Marsh ? Grass | 11 - Water - passable (yellow)
            Color iWaterImpassable = Color.Blue; // DeepWater | 12 - Water - impassable (blue)
            Color iRoof = Color.Pink; // ReservedBlocked | 13 - Roof - impassable (pink) ! not found
            Color iWorldmapExit = Color.Aqua; // ReservedBlocked? | 14 - Worldmap exit (light blue)
            Color iIce = Color.White; // Metal ? Stone | 15 - Grass (white)


            Color[] known = new Color[] { iObstacle , iSand, iWood1, iWood2, iStoneEcho, iGrass, iWater,
                iStoneHard, iFlyover, iWood, iWall, iSnow,
                iWaterImpassable, iRoof, iWorldmapExit, iIce};

            Color[] not_found = new Color[] { iWall, iRoof };

            using (Bitmap orig = (Bitmap)Bitmap.FromFile(origFilePath))
            {
                using (Bitmap sr = (Bitmap)Bitmap.FromFile(searchFileName))
                {
                    float ratioW = (float)sr.Width / orig.Width;
                    float ratioH = (float)sr.Height / orig.Height;
                    using (Bitmap outImg = new Bitmap(orig.Width, orig.Height))
                    {
                        for (int x = 0; x < outImg.Width; x++)
                            for (int y = 0; y < outImg.Height; y++)
                            {
                                //Color color = Color.Black;
                                int ox = (int)Math.Truncate(x * ratioW);
                                int oy = (int)Math.Truncate(y * ratioH);
                                Color px_sr = sr.GetPixel(ox, oy);
                                Color px = px_sr;
                                if (sr2)
                                {

                                }
                                else
                                {
                                    Color px_orig = orig.GetPixel(x, y);

                                    if (cek(px_sr, known))
                                    {
                                        if (cek(px_sr, not_found))
                                        {
                                            ;
                                        }

                                    }
                                    else
                                    {
                                        px_sr = Color.White;
                                    }

                                    byte alpha = 128 + 64;
                                    px = AlphaComposite(px_sr, px_orig, alpha);
                                }
                                outImg.SetPixel(x, y, px);
                            }

                        outImg.Save(outFileName);
                    }
                }
            }

        }

        static Size GetFileImageSize(string origFilePath)
        {
            Console.WriteLine(Path.GetFileName(origFilePath));
            using (Bitmap orig = (Bitmap)Bitmap.FromFile(origFilePath))
            {
                return orig.Size;
            }

        }

        static void Main(string[] args)
        {
            string origFilePath = args[0];
            origFilePath = @"D:\IE\Resources\IWD2\Maps\AR1000.bmp"; // iWood
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR6051.bmp"; // iStone
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR6050.bmp"; // iGrass
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR4101.bmp"; // iWater, iIce
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR5102.bmp"; // iWaterImpassable
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR1200.bmp"; // iWorldmapExit
            //origFilePath = @"D:\IE\Resources\IWD2\Maps\AR1001.bmp"; // iStoneHard, iObsticle

            //ProcessFile(origFilePath, true);
            if (true)
            {
                var files = Directory.GetFiles(@"D:\IE\Resources\IWD2\Maps", "*.bmp");
                int i = 0;
                int count = files.Length;
                List<string> toProcess = new List<string>();
                foreach (string filePath in files)
                {
                    i++;
                    string fileName = Path.GetFileName(filePath);
                    if (fileName.Length != 10) continue;
                    //if (fileName != "AR1002.bmp") continue;
                    toProcess.Add(filePath);
                }

                if (true)
                {
                    Parallel.ForEach(toProcess, filePath =>
                    {
                        ProcessFile(filePath, true);
                    });
                }

                if (false)
                {
                    List<Tuple<int, string>> fileSizes = new List<Tuple<int, string>>();
                    Parallel.ForEach(toProcess, filePath =>
                    {
                        Size s = GetFileImageSize(filePath);
                        lock (fileSizes) {
                            fileSizes.Add(new Tuple<int, string>(s.Width*s.Height, Path.GetFileName(filePath)));
                        }
                    });

                    var item = fileSizes.ArgMax(t => t.Item1);
                    Console.WriteLine($"Largest Map: {item.Item2}"); // AR4103.bmp 3x3
                }
            }

        }
    }

    public static class EnumerableExtensions
    {
        public static T ArgMax<T, K>(this IEnumerable<T> source,
                                     Func<T, K> map,
                                     IComparer<K> comparer = null)
        {
            if (Object.ReferenceEquals(null, source))
                throw new ArgumentNullException("source");
            else if (Object.ReferenceEquals(null, map))
                throw new ArgumentNullException("map");

            T result = default(T);
            K maxKey = default(K);
            Boolean first = true;

            if (null == comparer)
                comparer = Comparer<K>.Default;

            foreach (var item in source)
            {
                K key = map(item);

                if (first || comparer.Compare(key, maxKey) > 0)
                {
                    first = false;
                    maxKey = key;
                    result = item;
                }
            }

            if (!first)
                return result;
            else
                throw new ArgumentException("Can't compute ArgMax on empty sequence.", "source");
        }
    }
}
