using EnvDTE;
using Microsoft.VisualStudio.TemplateWizard;
using System;
using System.Collections.Generic;
using System.IO;

namespace PS4SPRXWizard
{
    public class ScriptCopyWizard : IWizard
    {
        private string _solutionDir;
        private string _templateDir;

        public void RunStarted(object automationObject, Dictionary<string, string> replacementsDictionary, WizardRunKind runKind, object[] customParams)
        {
            _solutionDir = replacementsDictionary["$solutiondirectory$"];
            _templateDir = Path.GetDirectoryName((string)customParams[0]);
        }

        public void RunFinished()
        {
            try
            {
                // Create External folder
                Directory.CreateDirectory(Path.Combine(_solutionDir, "External"));

                // Copy Scripts folder
                string sourceScripts = Path.Combine(_templateDir, "Scripts");
                string destScripts = Path.Combine(_solutionDir, "Scripts");

                if (Directory.Exists(sourceScripts))
                {
                    Directory.CreateDirectory(destScripts);
                    foreach (string file in Directory.GetFiles(sourceScripts))
                    {
                        File.Copy(file, Path.Combine(destScripts, Path.GetFileName(file)), true);
                    }
                }
            }
            catch { }
        }

        public void ProjectFinishedGenerating(Project project) { }
        public void ProjectItemFinishedGenerating(ProjectItem projectItem) { }
        public void BeforeOpeningFile(ProjectItem projectItem) { }
        public bool ShouldAddProjectItem(string filePath) => true;
    }
}