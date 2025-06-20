#pragma once

#include "IR.h"

class VelvetReverb
{
    public: 
        VelvetReverb();
        ~VelvetReverb();

        VelvetReverb(const VelvetReverb&) = delete;
        VelvetReverb(VelvetReverb&&) = delete;
        const VelvetReverb& operator=(const VelvetReverb&) = delete;
        const VelvetReverb& operator=(VelvetReverb&&) = delete;

        void prepare(double newSampleRate);
        void process();

    private: 
        static constexpr auto VN_IR = IR;
        static constexpr auto IR_LENGTH = IR_length;

        double sampleRate = { 48000.f };


};