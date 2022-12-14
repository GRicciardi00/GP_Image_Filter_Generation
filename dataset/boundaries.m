inputFolder = '/Users/giuseppericciardi/Downloads/BSR 3/BSDS500/data/groundTruth/val';
outputFolder = '/Users/giuseppericciardi/Downloads/BSR 3/BSDS500/data/groundTruth/val_exported'; % Please change, if needed.
fileList = dir(fullfile(inputFolder,'*.mat'));
for kk = 1:numel(fileList)
  S = load(fullfile(fileList(kk).folder,fileList(kk).name));
  I = S.groundTruth{1,1}.Boundaries;
  fileName = replace(fileList(kk).name,'.mat','.tiff');
  imwrite(I,fullfile(outputFolder,fileName));
end